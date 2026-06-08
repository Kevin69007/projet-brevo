---
name: Hub Brevo — sous-projet Cuspide warmup news.cuspide.fr
description: Hub Brevo multi-sociétés ; sous-projet Cuspide bloqué à 58% spam rate après 40j (DKIM+DMARC absents) ; plan 3 phases approuvé 05/05/2026
type: project
originSessionId: b99f8f53-147b-41ab-96a7-bc601217366f
---
# Hub Brevo email — structure multi sous-projets

Le **skill `/projet-brevo`** est un hub d'envoi email Brevo qui gère **plusieurs sous-projets indépendants** (un par société/domaine émetteur). Chaque sous-projet = sa propre mailbox, son propre warmup Allegrow, sa propre liste contacts, ses propres campagnes.

**Sous-projets :**
- **Cuspide** (sous-projet 1, ACTIF, bloqué) — détaillé ci-dessous. Domaine émetteur : `news.cuspide.fr`
- **À venir** : autres sociétés du groupe (JAK Formation, Pumpy, AS Travaux, Wei-Wei, Padelstars, etc.) selon priorités. Chaque future société aura son propre sous-domaine + warmup + config Brevo.

Les fichiers de config par sous-projet vivent dans `~/.claude/skills/projet-brevo/context/config/` (un fichier par société à terme — actuellement seul `brevo-config.md` Cuspide existe).

# Sous-projet Cuspide — diagnostic 05/05/2026

## État
- Mailbox `contact@news.cuspide.fr` (IONOS Mail Basic) connectée à Allegrow le **26/03/2026**
- Après 40 jours : **reputation 41.56% / spam rate 58.44%** (visible https://app.neverspam.io/user/mailboxes)
- Gate Brevo : <5% sur 7 jours consécutifs → **non atteint, blocage étape 7+ projet Brevo**
- Étape projet Brevo : **bloquée à l'étape 6/9** (skill `/projet-brevo`)

## Root cause (audit DNS 05/05/2026)
- SPF ✅ `v=spf1 include:_spf-eu.ionos.com ~all`
- **DKIM ❌** — aucun sélecteur trouvé sur news.cuspide.fr (testé s1, s2, ionos, default, selector1, selector2, dkim, k1, mail)
- **DMARC ❌** — aucun record `_dmarc.news.cuspide.fr`
- **DMARC parent (cuspide.fr) cassé** : `rua=mailto:postmaster@exemple.com` (placeholder copié de doc, jamais corrigé)

→ 40 jours de warmup avec emails non signés DKIM = on a entraîné Gmail/Yahoo (politique 02/2024) à classer le domaine en spam. Le bilan du 26/03 affirmait "DKIM ✅ DMARC ✅" — c'était **faux**, jamais vérifié par `dig`.

**Why:** Bilan textuel rédigé sans audit DNS effectif. Personne n'avait fait `dig TXT _dmarc.news.cuspide.fr` ni cherché les sélecteurs DKIM avant de lancer le warmup.
**How to apply:** Toujours `dig` avant de capitaliser un état "DNS OK" dans un bilan ou rapport.

## Plan approuvé (05/05/2026)

### Phase 1 — Fix DNS (à faire en priorité)
1. Activer DKIM IONOS pour news.cuspide.fr (panel Email → Sécurité)
2. Ajouter record DKIM via IONOS DNS API (clé `claude-dns`, zone ID `6a9b6398-2cf9-11ec-bda4-0a5864441f49`)
3. Créer DMARC sur `_dmarc.news.cuspide.fr` : `v=DMARC1; p=none; pct=100; rua=mailto:dmarc@cuspide.fr; ruf=mailto:dmarc@cuspide.fr; aspf=r; adkim=r`
4. Corriger DMARC parent `_dmarc.cuspide.fr` (rua bidon → `dmarc@cuspide.fr`)
5. Vérifier `dig` + mxtoolbox + mail-tester (>8/10 visé)

### Phase 2 — Reset warmup (J+0 à J+28 après fix DNS)
- Cibles : <20% J+14, <10% J+21, <5% J+28
- Logger checks weekly dans `~/.claude/skills/expert-delivrabilite-email/context/mailboxes-status.md`

### Phase 3 — Plan B (si stagne >20% à J+21)
- **A** : nouvelle mailbox + sous-domaine neuf (`email.cuspide.fr`) + warmup from scratch
- **B** : envoi via Brevo SMTP direct (exploite leur infra DKIM/SPF, news.cuspide.fr juste From-domain)

## Fichiers de référence
- Plan complet : `~/.claude/plans/tu-peux-me-faire-federated-peach.md`
- Skill projet : `~/.claude/skills/projet-brevo/SKILL.md`
- Skill délivrabilité : `~/.claude/skills/expert-delivrabilite-email/`
- Mailboxes status (à corriger ligne 9 — DNS marqué OK alors qu'incomplet) : `~/.claude/skills/expert-delivrabilite-email/context/mailboxes-status.md`
