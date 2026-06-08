"""Parse les XML DMARC et stocke en SQLite."""
import logging
import sqlite3
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import Iterator, Tuple

from db import report_exists

log = logging.getLogger(__name__)


def _text(element, tag: str, default: str = "") -> str:
    if element is None:
        return default
    found = element.find(tag)
    if found is None or found.text is None:
        return default
    return found.text.strip()


def parse_xml_to_db(conn: sqlite3.Connection, source_mailbox: str, xml_bytes: bytes) -> Tuple[bool, str]:
    """Parse un XML et insère en DB. Retourne (inserted, report_id_str)."""
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError as e:
        log.warning(f"XML invalide: {e}")
        return False, ""

    metadata = root.find("report_metadata")
    policy = root.find("policy_published")
    if metadata is None or policy is None:
        log.warning("XML sans report_metadata ou policy_published")
        return False, ""

    report_id_str = _text(metadata, "report_id")
    if not report_id_str:
        log.warning("XML sans report_id")
        return False, ""

    if report_exists(conn, report_id_str):
        log.debug(f"Report {report_id_str} déjà en DB, skip")
        return False, report_id_str

    org_name = _text(metadata, "org_name")
    org_email = _text(metadata, "email")
    domain = _text(policy, "domain")

    date_range = metadata.find("date_range")
    date_begin = int(_text(date_range, "begin", "0"))
    date_end = int(_text(date_range, "end", "0"))

    policy_p = _text(policy, "p")
    policy_sp = _text(policy, "sp")
    policy_pct = int(_text(policy, "pct", "100"))

    fetched_at = datetime.utcnow().isoformat()

    cur = conn.execute(
        """
        INSERT INTO reports (org_name, org_email, domain, report_id, date_begin, date_end,
                             policy_p, policy_sp, policy_pct, fetched_at, source_mailbox)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (org_name, org_email, domain, report_id_str, date_begin, date_end,
         policy_p, policy_sp, policy_pct, fetched_at, source_mailbox),
    )
    report_db_id = cur.lastrowid

    for record in root.findall("record"):
        row = record.find("row")
        identifiers = record.find("identifiers")
        auth = record.find("auth_results")
        policy_eval = row.find("policy_evaluated") if row is not None else None

        source_ip = _text(row, "source_ip")
        count = int(_text(row, "count", "0"))
        disposition = _text(policy_eval, "disposition")
        dkim_eval = _text(policy_eval, "dkim")
        spf_eval = _text(policy_eval, "spf")
        header_from = _text(identifiers, "header_from")

        # auth_results peut contenir plusieurs <dkim> et <spf>. On stocke le premier de chaque.
        dkim = auth.find("dkim") if auth is not None else None
        spf = auth.find("spf") if auth is not None else None

        dkim_domain = _text(dkim, "domain")
        dkim_result = _text(dkim, "result")
        dkim_selector = _text(dkim, "selector")
        spf_domain = _text(spf, "domain")
        spf_result = _text(spf, "result")

        conn.execute(
            """
            INSERT INTO records (report_id, source_ip, count, disposition,
                                 dkim_eval, spf_eval, header_from,
                                 dkim_domain, dkim_result, dkim_selector,
                                 spf_domain, spf_result)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (report_db_id, source_ip, count, disposition,
             dkim_eval, spf_eval, header_from,
             dkim_domain, dkim_result, dkim_selector,
             spf_domain, spf_result),
        )

    conn.commit()
    return True, report_id_str


def parse_batch(conn: sqlite3.Connection, xml_iter: Iterator[Tuple[str, str, bytes]]) -> dict:
    stats = {"received": 0, "inserted": 0, "skipped_duplicate": 0, "errors": 0}
    for source_mailbox, fname, xml_bytes in xml_iter:
        stats["received"] += 1
        try:
            inserted, _ = parse_xml_to_db(conn, source_mailbox, xml_bytes)
            if inserted:
                stats["inserted"] += 1
            else:
                stats["skipped_duplicate"] += 1
        except Exception as e:
            log.error(f"Erreur parse {fname}: {e}")
            stats["errors"] += 1
    return stats
