"""Schéma SQLite et helpers."""
import sqlite3
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    org_name TEXT NOT NULL,
    org_email TEXT,
    domain TEXT NOT NULL,
    report_id TEXT NOT NULL UNIQUE,
    date_begin INTEGER NOT NULL,
    date_end INTEGER NOT NULL,
    policy_p TEXT,
    policy_sp TEXT,
    policy_pct INTEGER,
    fetched_at TEXT NOT NULL,
    source_mailbox TEXT
);

CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    report_id INTEGER NOT NULL REFERENCES reports(id) ON DELETE CASCADE,
    source_ip TEXT NOT NULL,
    count INTEGER NOT NULL,
    disposition TEXT,
    dkim_eval TEXT,
    spf_eval TEXT,
    header_from TEXT,
    dkim_domain TEXT,
    dkim_result TEXT,
    dkim_selector TEXT,
    spf_domain TEXT,
    spf_result TEXT
);

CREATE INDEX IF NOT EXISTS idx_records_report ON records(report_id);
CREATE INDEX IF NOT EXISTS idx_reports_domain ON reports(domain);
CREATE INDEX IF NOT EXISTS idx_reports_date ON reports(date_begin);
CREATE INDEX IF NOT EXISTS idx_records_source_ip ON records(source_ip);
"""


def get_conn(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    return conn


def report_exists(conn: sqlite3.Connection, report_id: str) -> bool:
    cur = conn.execute("SELECT 1 FROM reports WHERE report_id = ?", (report_id,))
    return cur.fetchone() is not None
