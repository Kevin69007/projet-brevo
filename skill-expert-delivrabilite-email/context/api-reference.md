# API Reference — Delivrabilite Email

## IONOS DNS API

- **Base URL** : `https://api.hosting.ionos.com/dns/v1`
- **Auth** : `X-API-Key: ${IONOS_API_PREFIX}.${IONOS_API_SECRET}` (dans `~/.env.claude`)
- **Cle** : `claude-dns` (creee 25/03/2026)

### Zones utiles

| Domaine | Zone ID |
|---------|---------|
| cuspide.fr | `6a9b6398-2cf9-11ec-bda4-0a5864441f49` |
| besmilecare.fr | `6a155934-d346-11ef-9c3d-0a586444165c` |
| formations-dentaire.fr | `0e6f475d-fdbb-11ef-94cb-0a5864440408` |
| jak-company.com | `f6ca326e-3995-11ed-9071-0a58644410c2` |
| wei-wei.fr | `65ca04de-19b4-11ee-a21f-0a5864440ce1` |

### Endpoints

```bash
KEY="${IONOS_API_PREFIX}.${IONOS_API_SECRET}"
BASE="https://api.hosting.ionos.com/dns/v1"

# Lister toutes les zones
curl -s -X GET "$BASE/zones" -H "X-API-Key: $KEY"

# Voir records d'une zone
curl -s -X GET "$BASE/zones/{zoneId}" -H "X-API-Key: $KEY"

# Ajouter records (PATCH — ajoute sans supprimer les existants)
curl -s -X PATCH "$BASE/zones/{zoneId}" -H "X-API-Key: $KEY" \
  -H "Content-Type: application/json" -d '[{"name":"sub.domain.fr","type":"TXT","content":"\"value\"","ttl":3600,"prio":0,"disabled":false}]'

# ⚠️ PUT ecrase TOUT — NE JAMAIS UTILISER SANS BACKUP
```

### SSH (fichiers web uniquement, PAS DNS)
```bash
ssh ionos-wp  # Host dans ~/.ssh/config → u98088930@access792769250.webspace-data.io
```

## Brevo API

- **Base URL** : `https://api.brevo.com/v3`
- **Auth** : `api-key: ${BREVO_API_KEY}` (dans `~/.env.claude`)
- **Cle** : `claude-email` (creee 25/03/2026), format `xkeysib-...`
- **Compte** : Cuspide | 9 975 credits | 11 352 contacts

### Endpoints delivrabilite

```bash
# Infos compte
curl -s "$BASE/account" -H "api-key: $KEY"

# Lister domaines + statut authentification
curl -s "$BASE/senders/domains" -H "api-key: $KEY"

# Lister senders
curl -s "$BASE/senders" -H "api-key: $KEY"

# Lister listes de contacts
curl -s "$BASE/contacts/lists" -H "api-key: $KEY"

# Creer campagne email (DRAFT)
curl -s -X POST "$BASE/emailCampaigns" -H "api-key: $KEY" -H "Content-Type: application/json" -d '{...}'

# Envoyer campagne
curl -s -X POST "$BASE/emailCampaigns/{id}/sendNow" -H "api-key: $KEY"
```

## EmailListValidation API

- **Base URL** : `https://app.emaillistvalidation.com/api`
- **Auth** : `secret` param (dans `~/.env.claude` → `EMAILLISTVALIDATION_API_KEY`)

```bash
# Valider un email unique
curl "https://app.emaillistvalidation.com/api/verifEmail?secret=$KEY&email=test@example.com"
# Reponse : ok, fail, unknown, spamtrap, abuse, do_not_mail, disposable

# Valider une liste (upload CSV)
curl -X POST "https://apps.emaillistvalidation.com/api/verifApiFile" \
  -F "secret=$KEY" -F "filename=@contacts.csv"
```

## Allegrow/Neverspam

- **API Base URL** : `https://api.allegrow.co`
- **Auth** : `x-api-key: ${ALLEGROW_API_KEY}` (dans `~/.env.claude`)
- **Key ID** : `${ALLEGROW_API_KEY_ID}` (identifiant admin, pas utilise dans les requetes)
- **Compte** : AppSumo Premium, 2500 credits
- **Docs** : https://docs.allegrow.co
- **UI** : https://app.neverspam.io (Chrome MCP pour warmup/mailboxes)

### API — Validation email (seul usage API)

```bash
# Validation synchrone
curl -X POST https://api.allegrow.co/v1/email/validate \
  -H "x-api-key: $ALLEGROW_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com"}'
# → {"requestId":"...","email":"...","allegrowStatus":"safe"}

# Validation async (webhook)
curl -X POST https://api.allegrow.co/v1/email/validate-async \
  -H "x-api-key: $ALLEGROW_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "webhookUrl": "https://..."}'
# → 202 + {"requestId":"...","message":"Email validation request accepted"}
```

### allegrowStatus — Actions

| Status | Signification | Action |
|--------|--------------|--------|
| `safe` | Valide, safe to send | Envoyer |
| `block_bounce_risk` | Invalide, va bouncer | Supprimer |
| `dead_email` | Invalide mais catch-all | Supprimer |
| `do_not_mail_abuse` | Risque spam complaint | Ne pas emailer |
| `spamtrap` | Piege a spam | **SUPPRIMER + ALERTER** |
| `some_risk` | Inconclusif | Retester dans 30 jours |
| `more_time_required` | Sync only, encore en cours | Retenter ou utiliser async |

### Limites API
- Quota mensuel (selon plan) — depassement → 400
- Rate limit par seconde — depassement → 429

### Ce qui n'est PAS dans l'API (Chrome MCP uniquement)
- Gestion des mailboxes (ajout/suppression)
- Activation/desactivation du warmup
- Consultation reputation/spam rate
- Astuce UI : bouton "Edit" en haut a droite → "Delete Mailbox" / "Update Credentials"

## Proxy-IPv4

- Dashboard : https://proxy-ipv4.com/en/dashboard/
- Doc API : https://docs.proxy-ipv4.com/
- Bot Telegram : https://t.me/IPv4TelegramBot
- Usage : proxies residentiels pour LinkedIn outreach
