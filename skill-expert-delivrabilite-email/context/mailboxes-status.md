# Statut Mailboxes — Allegrow/Neverspam

> Derniere mise a jour : 5 mai 2026 (post-fix DNS)

## ACTIF — news.cuspide.fr ⏳ WARMUP — DNS FIXÉ, RESET PHASE 2 EN COURS

| Mailbox | Statut | Warmup | DNS | Brevo |
|---------|--------|--------|-----|-------|
| contact@news.cuspide.fr | ✅ CONNECTEE | ⏳ Reset à J+0 le 05/05/2026 (post-fix DNS) | ✅ SPF / DKIM / DMARC | ✅ Authentifie |

### ✅ État DNS après fix (05/05/2026)
- SPF ✅ `v=spf1 include:_spf-eu.ionos.com ~all`
- DKIM ✅ 3 sélecteurs CNAME publiés : `s1-ionos`, `s2-ionos`, `s42582890` (CNAME → `*.dkim.ionos.com`)
- DMARC ✅ `_dmarc.news.cuspide.fr` = `v=DMARC1; p=none; pct=100; rua=mailto:dmarc@cuspide.fr; ruf=mailto:dmarc@cuspide.fr; aspf=r; adkim=r`
- DMARC parent ✅ corrigé (placeholder `postmaster@exemple.com` → `dmarc@cuspide.fr`)

### Historique audit DNS (avant fix)
- Diagnostic initial du 26/03 affirmait "DNS OK" sans audit `dig` réel.
- Audit dig du 05/05 a révélé l'absence de DMARC sous-domaine et l'absence du sélecteur DKIM dynamique `s42582890` (les `s1-ionos`/`s2-ionos` étaient présents).
- Conséquence : 40 jours de warmup avec authentification incomplète → Gmail/Yahoo (politique 02/2024) ont classé le domaine en spam (reputation 41.56%, spam rate 58.44% au J+40).
- Fix appliqué via API IONOS DNS le 05/05 — propagation Google DNS confirmée immédiate.

### Stats Allegrow 05/05/2026
- news.cuspide.fr : reputation 41.56% / spam rate 58.44%
- besmilecare.fr : 47.50% / 52.50%
- support.besmilecare.fr : 66.43% / 33.57%
- mail.besmilecare.fr : 61.54% / 38.46%

### Plan de remédiation (cf. project_warmup_news_cuspide_fr.md)
1. Phase 1 (urgent) : activer DKIM IONOS + créer DMARC sous-domaine + corriger DMARC parent
2. Phase 2 : continuer warmup 28j avec DNS authentifie (cibles <20% J+14, <10% J+21, <5% J+28)
3. Phase 3 si stagne : nouveau sous-domaine OU envoi via Brevo SMTP direct

### Infos connexion IONOS
- IMAP : imap.ionos.fr:993 (SSL/TLS)
- SMTP : smtp.ionos.fr:587 (STARTTLS)
- Allegrow : warmup actif, donnees dispo apres 3 jours ouvrés
- Gate envoi : spam rate < 5% pendant 7 jours + 4 semaines min de warmup → reportée Phase 2 terminée

### Prochaines actions
1. Creer mailbox dans IONOS (ou utiliser Brevo sender directement)
2. Ajouter dans Allegrow pour warmup
3. Suivre schedule warmup (voir warmup-schedules.md)

## MONITORING PASSIF — besmilecare.fr (on touche pas)

| Mailbox | Domaine | Dernier spam rate | Statut |
|---------|---------|-------------------|--------|
| amine@besmilecare.fr | besmilecare.fr | 71.43% rep / 28.57% spam | Monitoring |
| contact@support.besmilecare.fr | support.besmilecare.fr | 35% rep / 65% spam | Monitoring |
| kevin@mail.besmilecare.fr | mail.besmilecare.fr | (a verifier) | Monitoring |

## SUPPRIMES d'Allegrow (25/03/2026)

| Mailbox | Raison |
|---------|--------|
| contact@jak-company.com | Config issue, domaine plus utilise |
| contact@partenariat.wei-wei.fr | Carbonisee (56.56% spam) |

## Compte Allegrow
- Plan : AppSumo Premium (2500 credits)
- API : pas disponible (Chrome MCP uniquement)
- App : https://app.neverspam.io
- Slots liberes : 2 (apres suppression jak + wei-wei)

## Historique
- 23/03/2026 : Audit initial, toutes mailboxes en alerte rouge
- 24/03/2026 : Decision quarantaine totale, restart from zero
- 25/03/2026 : Suppression jak + wei-wei d'Allegrow, creation news.cuspide.fr, DNS configures, Brevo authentifie
