# Plan — Remédiation warmup news.cuspide.fr

## Context
Warmup Allegrow lancé le 26/03/2026 sur `contact@news.cuspide.fr` pour préparer les envois Brevo Cuspide. Bilan du 26/03 affirmait "SPF ✅ DKIM ✅ DMARC ✅". 40 jours plus tard (05/05), Allegrow remonte un **spam rate de 58.44%** (reputation 41.56%) — incompatible avec le gate <5% requis pour démarrer les campagnes.

Investigation DNS (`dig` 05/05) :
- SPF ✅ `v=spf1 include:_spf-eu.ionos.com ~all`
- **DKIM ❌** aucun sélecteur trouvé (testé : s1, s2, ionos, default, selector1, selector2, dkim, k1, mail)
- **DMARC ❌** aucun record sur `_dmarc.news.cuspide.fr`
- **DMARC parent (cuspide.fr) cassé** : `rua=mailto:postmaster@exemple.com` (placeholder copié de doc)

Conséquence : 40 jours de warmup avec emails non signés DKIM → Gmail/Yahoo (politique 02/2024 : DKIM+DMARC obligatoires) ont entraîné leur classifier à marquer `news.cuspide.fr` comme spam.

## Phase 1 — Fix DNS (aujourd'hui)
1. **Activer DKIM IONOS** pour le domaine email `news.cuspide.fr` :
   - IONOS Panel → Email → Domaines → `news.cuspide.fr` → Sécurité → Activer DKIM
   - Récupérer le record TXT généré (sélecteur dynamique IONOS, type `s<id>._domainkey`)
2. **Ajouter le record DKIM** dans la zone DNS via IONOS DNS API (clé `claude-dns`, zone ID `6a9b6398-2cf9-11ec-bda4-0a5864441f49`)
3. **Créer DMARC sur `_dmarc.news.cuspide.fr`** :
   ```
   v=DMARC1; p=none; pct=100; rua=mailto:dmarc@cuspide.fr; ruf=mailto:dmarc@cuspide.fr; aspf=r; adkim=r
   ```
4. **Corriger DMARC parent `_dmarc.cuspide.fr`** : remplacer `postmaster@exemple.com` par `dmarc@cuspide.fr` (créer mailbox si absente)
5. **Vérification** : `dig`, mxtoolbox.com, mail-tester.com (envoi test depuis `contact@news.cuspide.fr` → score visé >8/10)

## Phase 2 — Reset warmup (J+0 à J+28 après fix DNS)
Continuer le warmup sur la mailbox actuelle. Allegrow émettra désormais des messages authentifiés.
- Check weekly via app.neverspam.io/user/mailboxes
- Cibles : spam rate <20% à J+14, <10% à J+21, <5% à J+28
- Logger chaque check dans `expert-delivrabilite-email/context/mailboxes-status.md`

## Phase 3 — Plan B si Phase 2 stagne (>20% à J+21)
La mailbox a 40 jours de signaux négatifs accumulés chez Gmail. Deux options :
- **A — Nouvelle mailbox + sous-domaine** : `email.cuspide.fr` ou `mail.cuspide.fr`, DNS complet d'entrée (SPF+DKIM+DMARC), warmup 4 semaines from scratch
- **B — Envoi via Brevo SMTP direct** : exploite leur infra (DKIM/SPF Brevo), `news.cuspide.fr` sert juste de From-domain authentifié. Plus rapide mais moins de contrôle. À privilégier si urgence campagne.

## Fichiers critiques à modifier
- `~/.claude/skills/expert-delivrabilite-email/context/mailboxes-status.md` (corriger ligne 9 : DNS marqué OK alors qu'incomplet)
- `~/.claude/skills/expert-delivrabilite-email/context/dns-records.md` (ajouter section news.cuspide.fr réelle)
- IONOS zone cuspide.fr (records DKIM + DMARC sur sous-domaine news + correction DMARC parent)

## Outils existants à réutiliser
- **IONOS DNS API** (`~/.env.claude` → `IONOS_API_PREFIX`/`IONOS_API_SECRET`) — déjà documentée pour add records
- **Skill `/expert-delivrabilite-email`** — checklist DNS complète + warmup-schedules.md
- **Allegrow dashboard** : https://app.neverspam.io/user/mailboxes (API stats indisponible — dashboard web obligatoire)

## Vérification end-to-end
1. Après Phase 1 : `dig TXT _dmarc.news.cuspide.fr` + `dig TXT <selector>._domainkey.news.cuspide.fr` doivent renvoyer les records
2. mail-tester.com depuis `contact@news.cuspide.fr` → score >8/10
3. Hebdo Allegrow : courbe reputation remonte
4. Gate de passage Phase 4 (étape 7+ du projet Brevo) : 7 jours consécutifs spam rate <5%

## À capitaliser en mémoire (à exécuter après ExitPlanMode)
- `project_warmup_news_cuspide_fr.md` — état + plan 3 phases + dates
- `feedback_audit_dns_avant_warmup.md` — toujours `dig` SPF+DKIM+DMARC AVANT lancement, ne pas faire confiance au bilan textuel
- `reference_allegrow_dashboard.md` — URL `app.neverspam.io/user/mailboxes`, pas d'API stats (403), login via `auth.allegrow.co`
- `troubleshooting-index.md` — entrée "Spam rate explosé après warmup → vérifier DKIM/DMARC en premier"
- Mise à jour `expert-delivrabilite-email/context/mailboxes-status.md` (correction état réel DNS)
