# Protocole de mise en place — Stratégie commerciale multi-canal

> Document de référence reproductible pour chaque société du groupe (Cuspide, Kelaj, Pumpy, AS Travaux, etc.)
> Version 1.0 — 7 mai 2026

---

## 1. Principe directeur

**Le warmup email = 28-35 jours = goulot d'étranglement #1.**

Tout ce qui peut être lancé en parallèle pendant ce warmup **doit l'être**. Sinon tu ajoutes 4 semaines de retard par négligence.

Trois autres temps d'attente critiques à anticiper :
1. **Pixels publicitaires** (Meta, Google) : 14-28 jours pour accumuler assez de data avant de pouvoir construire des audiences lookalike
2. **SEO** : 4-12 semaines pour qu'un nouveau contenu commence à ranker
3. **Bots & comptes sociaux** : 14-21 jours d'activité douce avant de pouvoir scale sans risque de ban

Le protocole ci-dessous lance **tous les chronos en parallèle dès J+0**.

---

## 2. Vue d'ensemble — Schéma temporel (8 semaines)

```
SEMAINE   1     2     3     4     5     6     7     8
─────────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────
EMAIL    │ DNS │ ════ WARMUP ALLEGROW ════│ ▶ Campagnes Brevo
         │ +Mbox│                          │
─────────┼─────┴─────┬─────────────────────┼─────────────
PIXELS   │ Install   │ Maturation (data)   │ ▶ Lookalikes prêts
─────────┼───────────┴─────────────────────┼─────────────
SOCIAL   │ Setup    Création contenu      │ ▶ Pub froide + retargeting
         │ comptes   organique chaud       │
─────────┼─────┬─────┬─────┬─────┬─────────┼─────────────
SCRAPING │ Setup│ ═══ Run + clean + valid │ ▶ DB exploitable
─────────┼─────┴─────┴─────┬───────────────┼─────────────
SEO      │ Audit + plan    │ Production rédac│ ▶ Indexation
         │                 │                 │   (suite >>)
─────────┼─────────────────┴─────────────────┼─────────────
PHONING  │                                   │ ▶ Sur DB qualifiée
─────────┼───────────────────────────────────┼─────────────
SMS/WA   │           Préparation             │ ▶ Sur DB qualifiée
─────────┼───────────────────────────────────┼─────────────
POSTAL   │              Préparation          │ ▶ Sur top-tier DB
─────────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────
        J+0   J+7  J+14  J+21  J+28  J+35  J+42  J+49
```

**Gates clés :**
- **J+14** : checkpoint warmup (cible <20% spam rate). Si stagne → décider Plan B (nouveau sous-domaine OU bascule Brevo SMTP direct)
- **J+28** : warmup OK (cible <5%). Démarrage gate 7-jours
- **J+35** : 1ères vraies campagnes email autorisées
- **J+42** : pixels assez mûrs pour lookalikes scalables

---

## 3. Phase 1 — FOUNDATIONS (J+0 à J+7)

**Objectif :** lancer tous les chronos longs en parallèle.

### 3.1 Email infrastructure

- [ ] Audit DNS via `dig` (SPF, DKIM IONOS 3 sélecteurs, DMARC sub + parent) — **NE JAMAIS sauter, leçon Cuspide**
- [ ] Création sous-domaine envoi (ex: `pros.<societe>.com`)
- [ ] Création mailbox warmup (ex: `contact@pros.<societe>.com`)
- [ ] Création mailbox `dmarc@<societe>.com`
- [ ] Configuration From-name (Display Name humain ou brand chaleureux)
- [ ] Push DNS via API IONOS : DKIM s42582890 + DMARC sous-domaine + correction DMARC parent
- [ ] Test mail-tester >8/10 (idéalement 10/10)
- [ ] Connexion mailbox dans Allegrow → **warmup démarre J+0**
- [ ] Authentifier le sous-domaine dans Brevo (Brevo SMTP records sur le sous-domaine)

**Dépendances aval :** rien ne bloque, lance immédiatement.

### 3.2 Pixels publicitaires (Meta + Google + TikTok + LinkedIn)

- [ ] Vérifier installation pixels sur tous les sites :
  - Meta Pixel
  - Google Tag (GA4 + Google Ads conversion)
  - TikTok Pixel
  - LinkedIn Insight Tag
- [ ] Configurer événements de conversion (achat, lead, formulaire)
- [ ] Configurer Conversion API (Meta CAPI) côté serveur pour fiabiliser malgré iOS 14+
- [ ] Vérifier que les pixels remontent du trafic existant (sinon corriger)

**Dépendances aval :** lookalikes demandent ~14j de data minimum. Plus tu retardes, plus tu reportes la possibilité de scale en pub froide.

### 3.3 Comptes sociaux (Meta, LinkedIn, TikTok, X, Snapchat)

- [ ] Audit comptes existants (cohérence visuelle, bio, liens)
- [ ] Création des comptes manquants
- [ ] Configurer Business Manager Meta + Business Manager LinkedIn
- [ ] Vérifier domaine dans Meta (pour CAPI + iOS 14)
- [ ] Préparer kit visuel (logos, couleurs, polices, templates posts)
- [ ] Configurer Metricool (skill `/projet-metricool` déjà en place) pour planification

**Dépendances aval :** la pub Meta/TikTok demande des comptes "warm" (au moins 14j d'activité organique). Sans ça, risque de ban + algorithme dégradé.

### 3.4 Scraping & base de données

- [ ] Définir le profil cible (vertical, taille, géographie, ICP)
- [ ] Setup Octoparse / Apify avec les sources :
  - Pages Jaunes / Annuaires métiers
  - LinkedIn Sales Navigator (via Apify)
  - Google Maps + sites pros
  - Listes spécifiques au vertical (ex: ordres professionnels)
- [ ] Configuration anti-détection (rotation IP, user-agent, délais humains)
- [ ] Setup pipeline : scraping → CSV brut → validation Email List Validation API (à toi de connecter ALLEGROW_API_KEY ou autre) → CRM/Brevo
- [ ] Setup sauvegarde mensuelle automatique de la BDD (Google Drive ou S3)

**Dépendances aval :** sans BDD propre, pas de cible pour les campagnes. Mais le scraping peut tourner pendant tout le warmup.

### 3.5 SEO — Audit & plan

- [ ] Audit du site existant (vitesse, mobile, schema markup, méta-données)
- [ ] Analyse mots-clés cibles (Ahrefs / SEMrush / Ubersuggest)
- [ ] Plan éditorial 12 semaines (1-3 articles/semaine min pour signal Google)
- [ ] Setup Search Console + Analytics
- [ ] **Référencement IA** : optimiser pour ChatGPT/Perplexity/Gemini :
  - Schema.org markup détaillé (Organization, FAQPage, Article)
  - Contenus question-réponse formatés
  - Citations claires des sources
  - Flux RSS/Atom pour signal de fraîcheur

**Dépendances aval :** SEO = horizon 4-12 semaines, démarrer J+0 obligatoire sinon retard cumulatif.

### 3.6 Tracking & attribution

- [ ] Setup Switchy (déjà dans la stack) pour shortlinks trackés
- [ ] UTM convention par canal (source/medium/campaign/content)
- [ ] Setup Looker Studio dashboard centralisé (toutes les sources)
- [ ] CRM / pipeline de leads (Brevo CRM ou autre)

---

## 4. Phase 2 — MATURATION + PRODUCTION (J+7 à J+28)

**Objectif :** pendant que les chronos tournent (warmup, pixels, SEO indexing), produire **massivement** le contenu et les assets nécessaires pour les phases d'activation.

### 4.1 Email — passif

- [ ] Check Allegrow hebdo (J+14, J+21)
- [ ] Vérifier rapports DMARC dans dmarc@<societe>.com (signal que les receveurs voient bien le domaine)
- [ ] **NE PAS envoyer de campagne**. Patience.

### 4.2 Email — préparation campagnes

- [ ] Rédiger les **5-10 templates email** (welcome, contenu valeur, offre, relance, désinscription propre)
- [ ] Créer les **séquences automation** dans Brevo (sans les activer)
- [ ] Préparer les **listes de segmentation** dans Brevo (par vertical, par fraîcheur, par engagement)
- [ ] Définir les **règles de désinscription** + lien clair (RGPD)

### 4.3 Social — production contenu

- [ ] Créer **30 jours de posts** organiques (pour Meta + LinkedIn + TikTok minimum)
- [ ] Programmer dans Metricool
- [ ] Démarrer publication dès J+7 pour faire chauffer les comptes
- [ ] Activer les bots de commentaires/likes ciblés (avec prudence — limiter à 20-30 actions/jour les 14 premiers jours)

### 4.4 Pub — créatives à préparer

- [ ] **Brief créatif** par persona / par vertical
- [ ] Production **5-10 visuels** par audience (statique + carrousel + vidéo court)
- [ ] **Copies** de 3 longueurs (court / moyen / long) pour A/B test
- [ ] Préparer audiences custom dans Meta/Google (sans encore lancer)

### 4.5 Scraping — exécution & nettoyage

- [ ] Lancer scraping sur le périmètre cible
- [ ] Validation des emails via Email List Validation API ou similaire
- [ ] Dédoublonnage croisé avec BDD existante
- [ ] Enrichissement (Dropcontact, Hunter, FullContact selon le vertical)
- [ ] Import segmenté dans Brevo (sans envoyer encore)

### 4.6 SEO — production

- [ ] Publication articles selon le plan éditorial (rythme régulier signal Google)
- [ ] Maillage interne entre articles
- [ ] Soumission sitemap à Google Search Console
- [ ] Première campagne backlinks (annuaires qualité + guest posting)

### 4.7 Influence & partenariats

- [ ] Identifier 20-30 micro/nano-influenceurs du vertical (via Modash, Heepsy, ou recherche manuelle)
- [ ] Outreach personnalisé (cycle de négo 2-6 semaines)
- [ ] Préparer les briefs et conditions

### 4.8 SMS / WhatsApp / Postal — préparation

- [ ] Configurer **Brevo SMS** (si volumes faibles) ou solution dédiée (Sarbacane, Esendex)
- [ ] **WhatsApp Business API** (via Brevo, Twilio ou WATI) — délai validation Meta : 5-10 jours
- [ ] **Postal** : choisir prestataire (Mediapost, La Poste Pro), préparer template visuel + base d'adresses
- [ ] Préparer scripts respectant la réglementation (opt-in, opt-out, mentions légales)

---

## 5. Phase 3 — ACTIVATION CONTRÔLÉE (J+28 à J+42)

**Objectif :** premiers envois réels, à VOLUME LIMITÉ, pour valider et collecter de la data sans cramer la reputation.

### 5.1 Email (post-gate warmup)

- [ ] **Validation gate** : 7 jours consécutifs spam rate <5% sur Allegrow
- [ ] Première campagne sur **petite portion qualifiée** (200-500 contacts max)
- [ ] Monitoring fin (open rate, clic, bounce, plainte, désinscription)
- [ ] Si OK → 2ème campagne sur 1 000-2 000 contacts
- [ ] Si OK → scaling progressif (max +50% par envoi)

### 5.2 Pub Meta/Google/TikTok/LinkedIn — lancement

- [ ] **Pub Bdd custom audience** (upload de la BDD scrapée vers Meta/LinkedIn) → conversion ratio attendu 30-60% match
- [ ] **Pub froide ciblage intérêt** sur petite audience (test 50-100€/jour par campagne pour collecter signaux)
- [ ] **Retargeting visiteurs site** (pixel mûr depuis J+14, suffisamment de data depuis J+28)
- [ ] Test 3-5 créatives en CBO (Campaign Budget Optimization)

### 5.3 SMS / WhatsApp première vague

- [ ] Envoi SMS sur **opt-in confirmés uniquement** (pas de scraping pour SMS — risque légal majeur)
- [ ] WhatsApp templates validés Meta (HSM)
- [ ] Tracking via Switchy

### 5.4 DM réseaux sociaux

- [ ] **Bots de scraping LinkedIn** : extraction prospects + visites profil + connexion
- [ ] **Bots d'activité** : like + commentaire + invitation (volume limité 20-30/jour)
- [ ] Cold outreach LinkedIn manuel sur top-prospects (max 10/jour pour éviter détection)
- [ ] Instagram DM via outil officiel ou semi-manuel

### 5.5 Phoning

- [ ] Sur les leads qui ont **engagé** (open email + clic ou inscription)
- [ ] Script qualifié, pas de cold call brut (sauf si la BDD est ultra-qualifiée + contexte légal OK)

### 5.6 Postal

- [ ] **Sur top 5-10% de la BDD** uniquement (coût élevé, 0,80-2€ par envoi)
- [ ] Cibler les leads chauds non répondus aux autres canaux

---

## 6. Phase 4 — SCALE (J+42 et au-delà)

**Objectif :** monter en volume sur ce qui a prouvé ROI positif.

### 6.1 Lookalikes & scaling pub

- [ ] **Lookalike 1%** sur les meilleurs convertis (pixel + email engagés)
- [ ] Scale budget +30%/semaine sur les campagnes positives
- [ ] **Pause** systématique des créatives sous benchmark (CTR, CPL)
- [ ] Renouvellement créatif toutes les 2 semaines (anti-fatigue)

### 6.2 Email — cadence régulière

- [ ] Newsletter hebdo (jour fixe, ex: jeudi 10h)
- [ ] Séquences automation activées (welcome, anniversaire, abandonné, réengagement)
- [ ] Segmentation comportementale (engagés / dormants / perdus)
- [ ] Réactivation des dormants à J+90 (campagne dédiée, sinon nettoyer)

### 6.3 SEO — itération

- [ ] Analyse performances (Search Console clic / impression / position)
- [ ] Optimisation contenus moyens (rewriting, ajout interne links)
- [ ] Nouveaux clusters de mots-clés selon ce qui ranke

### 6.4 Influence — activation

- [ ] Lancement collaborations avec influenceurs sélectionnés
- [ ] Code promo / lien affilié trackés (Switchy)
- [ ] Reporting et reconduction des plus performants

### 6.5 Bot scaling

- [ ] Augmentation graduelle volume bots (max +20%/semaine)
- [ ] Multi-comptes pour répartir le risque (3-5 comptes par plateforme)
- [ ] Diversification fingerprints (multi-IP, multi-browsers)

---

## 7. Multi-sociétés — Réplication

Le hub gère plusieurs sociétés du groupe. Le protocole se réplique **entité par entité**, mais avec des choix structurants :

### 7.1 Parallèle vs séquentiel

| Approche | Pour | Contre |
|---|---|---|
| **2-3 sociétés en parallèle** | Optimise le temps d'attente warmup (le plus long) | Demande beaucoup de bande passante côté Kevin (production contenu × N) |
| **Séquentiel 1 par 1** | Permet d'industrialiser au fur et à mesure | Chaque société = 8 semaines minimum, total 6-12 mois |

**Recommandation pour le groupe Cuspide/JAK** : **lancer 2 sociétés en parallèle max**, jamais plus. Cuspide + Kelaj actuellement = bon rythme.

### 7.2 Mutualisation possible

- ✅ Compte Allegrow (jusqu'à X mailboxes en simultané selon plan)
- ✅ Compte Brevo (limité par plan, 1 par société recommandé pour cloisonner reputation)
- ✅ Métricool (1 compte gère plusieurs marques)
- ✅ Octoparse / Apify (1 abonnement = N scrapings)
- ✅ BDD scraping mutualisable si verticaux proches
- ❌ Comptes pub Meta/Google : **dédiés par marque** (sinon mélange de pixels = catastrophe attribution)

### 7.3 Cadence de lancement société par société

| Mois | Action |
|---|---|
| M0-M1 | Société A : warmup + setup |
| M0-M2 | Société A : activation + scale |
| M1-M2 | Société B : warmup + setup en parallèle |
| M2-M3 | Société B : activation pendant que A est en optimisation |
| M3+ | Société C, D, E... un nouveau démarrage tous les 1-1.5 mois |

---

## 8. Gates de décision (résumé)

| Date | Quoi vérifier | Décision |
|---|---|---|
| J+7 | DNS auth OK + warmup démarré + pixels installés | Sinon : bloquer et corriger |
| J+14 | Spam rate <20% | Si stagne >30% → Plan B |
| J+21 | Spam rate <10% | Si stagne >20% → bascule Brevo SMTP ou nouveau sous-domaine |
| J+28 | Spam rate <5% | Démarrage gate 7-jours |
| J+35 | 7j consécutifs <5% | Première campagne autorisée |
| J+42 | Pixels mûrs (data acc.) | Lookalikes activables |
| J+56 | Premières conversions | Décision scale ou pivot |

---

## 9. Outils de référence (stack actuelle Cuspide/JAK)

| Catégorie | Outils en place |
|---|---|
| Email | Brevo (envoi), IONOS (mailbox), Allegrow (warmup), Email List Validation (validation) |
| Tracking | Switchy (shortlinks), Metricool (social), Looker Studio (dashboard) |
| Scraping | Octoparse, Apify, TexAu |
| CRM/Lead | Brevo CRM, Encharge (automation), FindThatLead (enrichissement) |
| Bot/Outreach | TexAu, ZeroWork, Marquiz (quiz/lead magnets) |
| Quiz/Lead magnets | Marquiz, Woorise |
| Content/Social | Metricool, Nexweave (perso vidéo) |
| Validation email | Allegrow API, Neverspam |
| Spam/SPF check | Mail-tester, MXToolbox |

---

## 10. Risques fréquents & comment les éviter

| Risque | Comment l'éviter |
|---|---|
| Croire un bilan "DNS OK" sans audit | **Toujours `dig` avant warmup** (leçon Cuspide) |
| Envoyer une campagne avant gate <5% | Discipliner : règle hard, pas de dérogation |
| Acheter une BDD non opt-in pour SMS | Risque CNIL + Orange/Bouygues blocking → ne jamais |
| Lancer pub froide sans pixel mûr | Budget cramé, audiences vides → attendre J+28 minimum |
| Bot LinkedIn à 200/jour dès le départ | Ban quasi-garanti → 20-30 max les 14 premiers jours |
| Mélanger pixels de plusieurs marques | Attribution illisible → 1 BM par marque obligatoire |
| Sauter le test mail-tester | Risque DKIM cassé silencieusement → toujours >8/10 avant warmup |
| Ne pas vérifier les rapports DMARC | Détection tardive d'usurpation → check hebdo dmarc@... |

---

## 11. Pour reprendre le protocole sur une nouvelle société

1. Lire ce document
2. Lire les mémoires `project_warmup_*` et `feedback_*` du projet
3. Démarrer Phase 1 = J+0
4. Logger l'avancement dans `skill-expert-delivrabilite-email/context/mailboxes-status.md`
5. À chaque gate, mettre à jour la mémoire correspondante
