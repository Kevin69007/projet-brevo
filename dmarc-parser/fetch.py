"""Téléchargement des emails DMARC depuis IMAP IONOS et extraction des XML."""
import email
import gzip
import imaplib
import io
import logging
import os
import zipfile
from email.message import Message
from typing import Iterator, Tuple

from config import (
    ARCHIVE_FOLDER,
    DMARC_SENDER_PATTERNS,
    DMARC_SUBJECT_PATTERNS,
    IMAP_HOST,
    IMAP_PORT,
    MAILBOXES,
)

log = logging.getLogger(__name__)


def is_dmarc_email(msg: Message) -> bool:
    sender = (msg.get("From") or "").lower()
    subject = (msg.get("Subject") or "")
    if any(p.lower() in sender for p in DMARC_SENDER_PATTERNS):
        return True
    if any(p in subject for p in DMARC_SUBJECT_PATTERNS):
        return True
    return False


def extract_xml_attachments(msg: Message) -> Iterator[Tuple[str, bytes]]:
    """Yield (filename, xml_bytes) for each XML attachment found."""
    for part in msg.walk():
        if part.get_content_maintype() == "multipart":
            continue
        filename = part.get_filename() or ""
        payload = part.get_payload(decode=True)
        if not payload:
            continue
        lower = filename.lower()

        if lower.endswith(".xml"):
            yield filename, payload
        elif lower.endswith(".gz"):
            try:
                yield filename[:-3], gzip.decompress(payload)
            except (OSError, gzip.BadGzipFile) as e:
                log.warning(f"Could not decompress gz attachment {filename}: {e}")
        elif lower.endswith(".zip"):
            try:
                with zipfile.ZipFile(io.BytesIO(payload)) as zf:
                    for inner in zf.namelist():
                        if inner.lower().endswith(".xml"):
                            with zf.open(inner) as f:
                                yield inner, f.read()
            except zipfile.BadZipFile as e:
                log.warning(f"Could not unzip attachment {filename}: {e}")


def ensure_archive_folder(imap: imaplib.IMAP4_SSL, folder: str) -> None:
    typ, _ = imap.list()
    existing = []
    if typ == "OK":
        for raw in _ or []:
            try:
                line = raw.decode() if isinstance(raw, bytes) else str(raw)
                # IONOS line format: ()  "/" "FolderName"
                if folder.lower() in line.lower():
                    existing.append(line)
            except Exception:
                pass
    if not existing:
        log.info(f"Creating IMAP folder '{folder}'")
        try:
            imap.create(folder)
            imap.subscribe(folder)
        except imaplib.IMAP4.error as e:
            log.warning(f"Could not create folder {folder} (peut déjà exister): {e}")


def fetch_mailbox(mailbox_cfg: dict, dry_run: bool = False) -> Iterator[Tuple[str, str, bytes]]:
    """Connecte à IMAP, yield (mailbox_email, xml_filename, xml_bytes), déplace mail vers ARCHIVE_FOLDER."""
    email_addr = mailbox_cfg["email"]
    password = os.environ.get(mailbox_cfg["password_env"])
    if not password:
        log.error(f"Pas de mot de passe pour {email_addr} (env {mailbox_cfg['password_env']} vide)")
        return

    log.info(f"IMAP: connexion à {email_addr}")
    try:
        imap = imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT)
        imap.login(email_addr, password)
    except imaplib.IMAP4.error as e:
        log.error(f"Échec login IMAP {email_addr}: {e}")
        return

    try:
        ensure_archive_folder(imap, ARCHIVE_FOLDER)
        imap.select("INBOX")

        typ, data = imap.search(None, "ALL")
        if typ != "OK":
            log.warning(f"Search ALL failed sur {email_addr}")
            return

        msg_ids = data[0].split()
        log.info(f"{email_addr}: {len(msg_ids)} messages dans INBOX")

        for msg_id in msg_ids:
            typ, msg_data = imap.fetch(msg_id, "(RFC822)")
            if typ != "OK" or not msg_data or not msg_data[0]:
                continue
            raw = msg_data[0][1]
            msg = email.message_from_bytes(raw)

            if not is_dmarc_email(msg):
                continue

            xml_count = 0
            for fname, xml_bytes in extract_xml_attachments(msg):
                xml_count += 1
                yield email_addr, fname, xml_bytes

            if xml_count == 0:
                log.debug(f"Pas de XML dans le mail {msg_id} de {msg.get('From')}")
                continue

            if not dry_run:
                # Copy + delete = move
                imap.copy(msg_id, ARCHIVE_FOLDER)
                imap.store(msg_id, "+FLAGS", "\\Deleted")

        if not dry_run:
            imap.expunge()
    finally:
        try:
            imap.close()
        except Exception:
            pass
        imap.logout()


def fetch_all(dry_run: bool = False) -> Iterator[Tuple[str, str, bytes]]:
    for mb in MAILBOXES:
        yield from fetch_mailbox(mb, dry_run=dry_run)
