"""Génération de rapports markdown à partir de la DB SQLite."""
import sqlite3
from datetime import datetime, timedelta, timezone
from pathlib import Path

from config import REPORTS_DIR

# Sources connues = identification automatique des IPs
KNOWN_SOURCES = {
    "212.227.": "IONOS Mail SMTP",
    "217.72.": "IONOS Mail SMTP",
    "82.165.": "IONOS Mail SMTP",
    "212.40.": "IONOS Mail SMTP",
    "54.240.": "Amazon SES (Resend / app)",
    "54.239.": "Amazon SES",
    "209.85.": "Google / Gmail forwarder",
    "64.233.": "Google / Gmail",
    "66.249.": "Google",
    "104.47.": "Microsoft 365 / Outlook",
    "40.92.": "Microsoft 365 / Outlook",
    "46.105.": "OVH dedicated server",
    "37.187.": "OVH",
    "192.95.": "OVH Canada",
    "168.245.": "Sendgrid",
    "149.72.": "Sendgrid",
    "18.": "AWS",
    "52.": "AWS",
    "44.": "AWS",
}


def identify_source(ip: str) -> str:
    for prefix, label in KNOWN_SOURCES.items():
        if ip.startswith(prefix):
            return label
    return "Inconnu"


def fmt_pct(num: int, total: int) -> str:
    if total == 0:
        return "0.0%"
    return f"{(num * 100 / total):.1f}%"


def report_for_period(conn: sqlite3.Connection, days: int = 7) -> str:
    """Génère un rapport markdown pour les N derniers jours."""
    now = datetime.now(timezone.utc)
    since_dt = now - timedelta(days=days)
    since_ts = int(since_dt.timestamp())

    lines = []
    lines.append(f"# Rapport DMARC — {days} derniers jours")
    lines.append("")
    lines.append(f"> Période : {since_dt.strftime('%Y-%m-%d')} → {now.strftime('%Y-%m-%d')} (UTC)")
    lines.append(f"> Généré le : {now.strftime('%Y-%m-%d %H:%M UTC')}")
    lines.append("")

    # Domains présents
    domains = conn.execute(
        "SELECT DISTINCT domain FROM reports WHERE date_begin >= ? ORDER BY domain",
        (since_ts,),
    ).fetchall()

    if not domains:
        lines.append("⚠️ Aucun rapport DMARC reçu sur cette période.")
        return "\n".join(lines)

    for d in domains:
        domain = d["domain"]
        lines.append(f"## 📊 {domain}")
        lines.append("")

        # Volume + conformité
        agg = conn.execute(
            """
            SELECT
                COUNT(DISTINCT r.id) AS nb_reports,
                COALESCE(SUM(rec.count), 0) AS total_emails,
                COALESCE(SUM(CASE WHEN rec.dkim_eval='pass' AND rec.spf_eval='pass' THEN rec.count ELSE 0 END), 0) AS both_pass,
                COALESCE(SUM(CASE WHEN rec.dkim_eval='pass' AND rec.spf_eval='fail' THEN rec.count ELSE 0 END), 0) AS dkim_only,
                COALESCE(SUM(CASE WHEN rec.dkim_eval='fail' AND rec.spf_eval='pass' THEN rec.count ELSE 0 END), 0) AS spf_only,
                COALESCE(SUM(CASE WHEN rec.dkim_eval='fail' AND rec.spf_eval='fail' THEN rec.count ELSE 0 END), 0) AS both_fail
            FROM reports r
            LEFT JOIN records rec ON rec.report_id = r.id
            WHERE r.domain = ? AND r.date_begin >= ?
            """,
            (domain, since_ts),
        ).fetchone()

        nb_reports = agg["nb_reports"]
        total = agg["total_emails"]
        both_pass = agg["both_pass"]
        dkim_only = agg["dkim_only"]
        spf_only = agg["spf_only"]
        both_fail = agg["both_fail"]
        dmarc_ok = both_pass + dkim_only + spf_only  # DMARC pass si DKIM OU SPF aligné

        lines.append(f"- **Rapports reçus** : {nb_reports}")
        lines.append(f"- **Volume emails** : {total}")
        lines.append(f"- **Conformité DMARC** : {fmt_pct(dmarc_ok, total)} ({dmarc_ok}/{total})")
        lines.append(f"  - ✅ DKIM + SPF tous deux OK : {both_pass} ({fmt_pct(both_pass, total)})")
        lines.append(f"  - ✅ DKIM seul OK (forwarding) : {dkim_only} ({fmt_pct(dkim_only, total)})")
        lines.append(f"  - ✅ SPF seul OK : {spf_only} ({fmt_pct(spf_only, total)})")
        lines.append(f"  - 🚨 DKIM + SPF tous deux FAIL : {both_fail} ({fmt_pct(both_fail, total)})")
        lines.append("")

        # Top sources
        lines.append("### Top sources d'envoi (volume)")
        lines.append("")
        lines.append("| Source IP | Volume | Identification | DMARC PASS |")
        lines.append("|---|---|---|---|")
        sources = conn.execute(
            """
            SELECT
                rec.source_ip,
                SUM(rec.count) AS vol,
                SUM(CASE WHEN rec.dkim_eval='pass' OR rec.spf_eval='pass' THEN rec.count ELSE 0 END) AS pass_vol
            FROM reports r
            JOIN records rec ON rec.report_id = r.id
            WHERE r.domain = ? AND r.date_begin >= ?
            GROUP BY rec.source_ip
            ORDER BY vol DESC
            LIMIT 15
            """,
            (domain, since_ts),
        ).fetchall()
        for s in sources:
            ip = s["source_ip"]
            vol = s["vol"]
            pass_vol = s["pass_vol"]
            label = identify_source(ip)
            pct = fmt_pct(pass_vol, vol)
            icon = "✅" if pass_vol == vol else ("⚠️" if pass_vol > 0 else "🚨")
            lines.append(f"| `{ip}` | {vol} | {label} | {icon} {pct} |")
        lines.append("")

        # 🚨 Alertes : émetteurs avec DMARC FAIL total
        alerts = conn.execute(
            """
            SELECT
                rec.source_ip,
                SUM(rec.count) AS vol,
                rec.spf_domain,
                rec.dkim_domain
            FROM reports r
            JOIN records rec ON rec.report_id = r.id
            WHERE r.domain = ? AND r.date_begin >= ?
                  AND rec.dkim_eval = 'fail' AND rec.spf_eval = 'fail'
            GROUP BY rec.source_ip, rec.spf_domain, rec.dkim_domain
            ORDER BY vol DESC
            LIMIT 10
            """,
            (domain, since_ts),
        ).fetchall()
        if alerts:
            lines.append("### 🚨 Alertes — émetteurs avec DMARC FAIL")
            lines.append("")
            lines.append("| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |")
            lines.append("|---|---|---|---|---|")
            for a in alerts:
                lines.append(
                    f"| `{a['source_ip']}` | {a['vol']} | {identify_source(a['source_ip'])} | "
                    f"`{a['spf_domain'] or '—'}` | `{a['dkim_domain'] or '—'}` |"
                )
            lines.append("")
            lines.append(
                "> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine "
                "sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation."
            )
            lines.append("")

        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def write_reports(conn: sqlite3.Connection, out_dir: Path = REPORTS_DIR) -> list:
    out_dir.mkdir(parents=True, exist_ok=True)
    written = []

    for days, label in [(7, "7-derniers-jours"), (30, "30-derniers-jours")]:
        content = report_for_period(conn, days=days)
        date_tag = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        filename = out_dir / f"rapport-{label}-{date_tag}.md"
        filename.write_text(content, encoding="utf-8")
        written.append(str(filename))

        # Aussi un alias "latest" sans date pour pouvoir y faire référence
        latest = out_dir / f"rapport-{label}-LATEST.md"
        latest.write_text(content, encoding="utf-8")

    return written
