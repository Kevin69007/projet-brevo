# DMARC Parser — Hub Brevo

Parser local pour les rapports DMARC quotidiens reçus dans les mailboxes `dmarc@*` du hub. Stdlib Python uniquement (aucune dépendance pip).

## Quoi

À chaque run, le script :
1. Se connecte via IMAP aux mailboxes `dmarc@cuspide.fr`, `dmarc@kelaj-company.com` (et tous les futurs domaines listés dans `config.py`)
2. Télécharge les emails DMARC, extrait les XML (zip/gz/raw)
3. Parse les XML, insère en SQLite (`dmarc-history.db`)
4. Déplace les emails traités vers le dossier IMAP `DMARCS`
5. Régénère 2 rapports markdown : 7 derniers jours + 30 derniers jours

Les rapports sont écrits dans `rapports/`. Les fichiers `*-LATEST.md` pointent toujours sur la dernière version.

## Pré-requis

- Python 3 (stdlib uniquement, déjà installé sur Mac)
- Mots de passe des mailboxes dans `brevo-secrets.env` :
  - `DMARC_MAILBOX_PASSWORD` (pour `dmarc@cuspide.fr`)
  - `KELAJ_DMARC_PASSWORD` (pour `dmarc@kelaj-company.com`)

## Usage manuel

```bash
cd /Users/mo/projects/projet-brevo
source brevo-secrets.env

# Test sans toucher aux mails (dry-run)
python3 dmarc-parser/run.py --dry-run --verbose

# Run réel (fetch + parse + déplace + rapports)
python3 dmarc-parser/run.py

# Run réel + ouverture auto du rapport dans l'app par défaut
python3 dmarc-parser/run.py --open

# Régénérer uniquement les rapports markdown depuis la DB
python3 dmarc-parser/run.py --report-only
```

## Ouverture automatique du rapport (cron)

Le cron passe `--open`, donc le fichier `rapport-7-derniers-jours-LATEST.md` s'ouvre automatiquement à 10h00 dans ton app par défaut pour les .md.

Pour changer l'app par défaut sur Mac (par ex pour utiliser Obsidian / Typora / VS Code au lieu de TextEdit) :
1. Clic droit sur n'importe quel fichier `.md` → **Lire les informations** (Cmd+I)
2. Section **Ouvrir avec :** → choisir l'app voulue
3. Cliquer **Tout modifier...** pour appliquer à tous les fichiers `.md`

## Activation du cron automatique (launchd Mac)

Le fichier `com.brevo.dmarc-parser.plist` est déjà prêt. Pour l'activer :

```bash
# Copier dans LaunchAgents (1 seule fois)
cp /Users/mo/projects/projet-brevo/dmarc-parser/com.brevo.dmarc-parser.plist \
   ~/Library/LaunchAgents/

# Charger (= activer)
launchctl load ~/Library/LaunchAgents/com.brevo.dmarc-parser.plist

# Vérifier qu'il est chargé
launchctl list | grep dmarc-parser
```

Pour désactiver :

```bash
launchctl unload ~/Library/LaunchAgents/com.brevo.dmarc-parser.plist
```

Pour modifier la config (ex: changer l'heure) :

```bash
launchctl unload ~/Library/LaunchAgents/com.brevo.dmarc-parser.plist
# Éditer le plist (changer Hour/Minute/Weekday)
launchctl load ~/Library/LaunchAgents/com.brevo.dmarc-parser.plist
```

**Cadence configurée :** Lundi à Vendredi à 10h00 (samedi/dimanche désactivés). Ordi doit être allumé à cette heure-là (sinon le run loupé n'est pas rattrapé).

## Logs

- `logs/run-YYYY-MM-DD.log` : log applicatif
- `logs/launchd.out.log` et `launchd.err.log` : sortie standard launchd

## Ajouter un nouveau domaine à monitorer

Éditer `config.py`, ajouter une entrée dans `MAILBOXES` :

```python
{
    "email": "dmarc@nouveau-domaine.fr",
    "password_env": "NOUVEAU_DMARC_PASSWORD",
    "domains": ["nouveau-domaine.fr", "pros.nouveau-domaine.fr"],
},
```

Puis ajouter le mot de passe dans `brevo-secrets.env` :

```bash
export NOUVEAU_DMARC_PASSWORD="..."
```

Et bien sûr modifier le DMARC `rua=mailto:dmarc@nouveau-domaine.fr` dans le DNS du domaine.

## Architecture des fichiers

```
dmarc-parser/
├── config.py                        # Config mailboxes + IMAP host
├── db.py                            # Schéma SQLite
├── fetch.py                         # IMAP + extraction XML
├── parse.py                         # XML → records DB
├── report.py                        # DB → markdown report
├── run.py                           # Orchestrateur (cron entry)
├── com.brevo.dmarc-parser.plist     # launchd config Mac
├── README.md                        # Ce fichier
├── dmarc-history.db                 # SQLite (créé au 1er run)
├── logs/                            # Logs run + launchd
└── rapports/                        # Rapports markdown générés
```

## Schéma SQLite

- `reports` : 1 ligne par fichier XML reçu (org, domain, period, policy)
- `records` : 1 ligne par bloc `<record>` (source_ip, count, DKIM/SPF/DMARC results)

Tu peux interroger directement avec sqlite3 :

```bash
sqlite3 dmarc-parser/dmarc-history.db
> SELECT domain, COUNT(*), SUM(count) FROM reports r JOIN records rec ON rec.report_id=r.id GROUP BY domain;
```

## Comportement de dédoublonnage

Le `report_id` est `UNIQUE` en DB. Si le script re-télécharge le même XML (ex: après un crash), il sera silencieusement skippé. Tu peux donc relancer sans risque.

## Comportement de déplacement

Les emails contenant un XML DMARC valide sont déplacés vers le dossier IMAP `DMARCS` (créé automatiquement s'il n'existe pas). Les emails sans XML valide restent dans INBOX.

`--dry-run` désactive le déplacement (les mails restent en INBOX).
