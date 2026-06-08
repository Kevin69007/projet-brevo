#!/usr/bin/env python3
"""Orchestrateur du parser DMARC. Appelé par cron quotidien."""
import argparse
import logging
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from config import DB_PATH, LOGS_DIR, REPORTS_DIR
from db import get_conn
from fetch import fetch_all
from parse import parse_batch
from report import write_reports


def setup_logging(verbose: bool = False) -> None:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOGS_DIR / f"run-{datetime.utcnow().strftime('%Y-%m-%d')}.log"

    handlers = [
        logging.FileHandler(log_path, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ]
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
        handlers=handlers,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="DMARC parser quotidien.")
    parser.add_argument("--dry-run", action="store_true",
                        help="Lit les emails IMAP mais ne les déplace pas.")
    parser.add_argument("--report-only", action="store_true",
                        help="Régénère les rapports markdown sans fetch/parse.")
    parser.add_argument("--open", action="store_true",
                        help="Ouvre le rapport 7-derniers-jours dans l'app par défaut à la fin (utile pour le cron).")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    setup_logging(verbose=args.verbose)
    log = logging.getLogger("run")

    log.info("=" * 60)
    log.info(f"Démarrage parser DMARC — {datetime.utcnow().isoformat()}Z")
    log.info(f"DB : {DB_PATH}")
    log.info(f"Rapports : {REPORTS_DIR}")
    if args.dry_run:
        log.info("⚠️ DRY RUN — aucun email ne sera déplacé")

    conn = get_conn(DB_PATH)

    if not args.report_only:
        log.info("Phase 1/3 — Fetch IMAP des nouveaux XML DMARC")
        xml_iter = fetch_all(dry_run=args.dry_run)

        log.info("Phase 2/3 — Parse + insertion en DB")
        stats = parse_batch(conn, xml_iter)
        log.info(
            f"Stats parse : reçus={stats['received']}, insérés={stats['inserted']}, "
            f"doublons={stats['skipped_duplicate']}, erreurs={stats['errors']}"
        )
    else:
        log.info("--report-only : skip fetch + parse")

    log.info("Phase 3/3 — Génération rapports markdown")
    written = write_reports(conn)
    for f in written:
        log.info(f"  → {f}")

    if args.open:
        latest_7d = REPORTS_DIR / "rapport-7-derniers-jours-LATEST.md"
        if latest_7d.exists():
            log.info(f"Ouverture (TextEdit + activate) : {latest_7d}")
            try:
                # 1. Open the file in TextEdit
                rc = subprocess.run(
                    ["open", "-a", "TextEdit", str(latest_7d)],
                    capture_output=True, text=True, timeout=10,
                )
                if rc.returncode != 0:
                    log.warning(f"open returncode={rc.returncode} stderr={rc.stderr}")

                # 2. Force TextEdit to come to the front (steals focus)
                applescript = 'tell application "TextEdit" to activate'
                subprocess.run(
                    ["osascript", "-e", applescript],
                    capture_output=True, text=True, timeout=10,
                )

                # 3. macOS notification to be safe (visible even if TextEdit is hidden)
                notif = (
                    'display notification "Nouveau rapport DMARC disponible" '
                    'with title "DMARC Parser" sound name "Glass"'
                )
                subprocess.run(
                    ["osascript", "-e", notif],
                    capture_output=True, text=True, timeout=10,
                )
            except Exception as e:
                log.warning(f"Échec ouverture : {e}")

    log.info("Fin parser DMARC ✅")
    log.info("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
