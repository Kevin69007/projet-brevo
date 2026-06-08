"""Configuration du parser DMARC."""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent
DB_PATH = BASE_DIR / "dmarc-history.db"
REPORTS_DIR = BASE_DIR / "rapports"
LOGS_DIR = BASE_DIR / "logs"

IMAP_HOST = "imap.ionos.fr"
IMAP_PORT = 993
ARCHIVE_FOLDER = "DMARCS"

MAILBOXES = [
    {
        "email": os.environ.get("DMARC_MAILBOX", "dmarc@cuspide.fr"),
        "password_env": "DMARC_MAILBOX_PASSWORD",
        "domains": ["cuspide.fr", "news.cuspide.fr"],
    },
    {
        "email": os.environ.get("KELAJ_DMARC_MAILBOX", "dmarc@kelaj-company.com"),
        "password_env": "KELAJ_DMARC_PASSWORD",
        "domains": ["kelaj-company.com", "pros.kelaj-company.com"],
    },
]

DMARC_SENDER_PATTERNS = [
    "noreply-dmarc-support@google.com",
    "dmarc-reports@",
    "dmarcreport@",
    "postmaster@",
    "@bounces.amazon.com",
    "no-reply@dmarc.yahoo.com",
    "dmarc_support@",
]

DMARC_SUBJECT_PATTERNS = [
    "Report Domain:",
    "Report-ID",
    "DMARC Aggregate Report",
    "Report domain:",
]
