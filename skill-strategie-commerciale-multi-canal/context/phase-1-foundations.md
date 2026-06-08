# Phase 1 — FOUNDATIONS (J+0 à J+7)

**Objectif :** lancer tous les chronos longs en parallèle.

## Email infrastructure (priorité #1)

- [ ] Audit DNS via `dig` (SPF, DKIM IONOS 3 sélecteurs `s1-ionos`/`s2-ionos`/`s42582890`, DMARC sub + parent)
- [ ] Création sous-domaine envoi (convention : `pros.<societe>.com` ou `mail.<societe>.com`)
- [ ] Création mailbox warmup (ex: `contact@pros.<societe>.com`)
- [ ] Création mailbox `dmarc@<societe>.com` pour rapports XML
- [ ] Configuration From-name (Display Name humain ou brand chaleureux)
- [ ] Push DNS via API IONOS : DKIM `s42582890` (toujours manquant sur sous-domaine) + DMARC sub + correction DMARC parent
- [ ] Test mail-tester >8/10 (idéalement 10/10)
- [ ] Connexion mailbox dans Allegrow → **warmup démarre J+0**
- [ ] Sauvegarde des credentials dans `brevo-secrets.env`

**Skill complementaire :** `/expert-delivrabilite-email` pour le détail technique.

## Pixels publicitaires

**Playbook détaillé :** `${CLAUDE_SKILL_DIR}/context/pixel-setup-playbook.md`

- [ ] Meta Pixel installé sur tous les sites (WordPress via PixelYourSite, Next.js via code custom)
- [ ] Google Tag (GA4 + Google Ads conversion)
- [ ] TikTok Pixel
- [ ] LinkedIn Insight Tag
- [ ] Conversion API Meta (CAPI) côté serveur (fiabilise iOS 14+)
- [ ] Événements de conversion configurés (achat, lead, formulaire, scroll, video view)
- [ ] **Vérification obligatoire** : Meta Pixel Helper + Events Manager confirment la remontée (sinon corriger AVANT de lancer pub)

**Distinction stack :**
- **WordPress/WooCommerce** → PixelYourSite (plugin) : base pixel + CAPI + Advanced Matching en quelques clics
- **Next.js/React custom** → Injection manuelle dans `<head>` + helpers `lib/tracking.js`

**Pourquoi en Phase 1 :** lookalikes demandent ~14j de data minimum. Plus tu retardes, plus tu reportes le scaling pub.

## Comptes sociaux

- [ ] Audit comptes existants (cohérence visuelle, bio, liens, mentions)
- [ ] Création comptes manquants (Meta, LinkedIn, TikTok, X, Snapchat selon vertical)
- [ ] Configurer Business Manager Meta + Business Manager LinkedIn
- [ ] Vérifier domaine dans Meta Business (pour CAPI + iOS 14)
- [ ] Préparer kit visuel (logos, couleurs, polices, templates posts)
- [ ] Setup Metricool (`/projet-metricool`) pour planification

**Pourquoi en Phase 1 :** comptes "warm" requis (14j+ d'activité organique). Sans ça, risque ban + algorithme dégradé sur la pub.

## Scraping & base de données

- [ ] Définir le profil cible (vertical, taille, géographie, ICP)
- [ ] Setup Octoparse / Apify avec sources :
  - Pages Jaunes / annuaires métiers
  - LinkedIn Sales Navigator (via Apify)
  - Google Maps + sites pros
  - Listes spécifiques au vertical (ordres professionnels, syndicats)
- [ ] Configuration anti-détection (rotation IP, user-agent, délais humains)
- [ ] Setup pipeline : scraping → CSV brut → validation Email List Validation → Brevo
- [ ] Sauvegarde mensuelle automatique (Google Drive / S3)

## SEO — Audit & plan

- [ ] Audit site (vitesse, mobile, schema markup, méta-données, sitemap)
- [ ] Analyse mots-clés cibles (Ahrefs, SEMrush, Ubersuggest)
- [ ] Plan éditorial 12 semaines (1-3 articles/semaine min pour signal Google)
- [ ] Setup Search Console + Analytics
- [ ] **Référencement IA** :
  - Schema.org markup détaillé (Organization, FAQPage, Article)
  - Contenus question-réponse formatés
  - Citations sources claires
  - Flux RSS/Atom pour signal de fraîcheur

## Tracking & attribution

- [ ] Setup Switchy pour shortlinks trackés
- [ ] UTM convention par canal (source/medium/campaign/content)
- [ ] Setup Looker Studio dashboard centralisé
- [ ] CRM / pipeline de leads (Brevo CRM ou autre)

## Validation Phase 1 — Critères pour passer Phase 2

- ✅ Warmup démarré dans Allegrow
- ✅ Mail-tester >8/10
- ✅ Pixels installés et trafic remonte
- ✅ Comptes sociaux opérationnels
- ✅ Scraping configuré (peut commencer à tourner)
- ✅ Plan SEO en place
- ✅ Tracking opérationnel

Si une de ces cases n'est pas cochée à J+7 → **bloquer et corriger** avant Phase 2.
