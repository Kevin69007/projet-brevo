# Formation IA — Architecture

## Produit
Formation à l'intelligence artificielle pour le secteur de l'architecture et du bâtiment : DAO/CAO assistée, optimisation énergétique, gestion de projet, conformité réglementaire.

## Site
- **Prod** : https://ia-en-architectes.kelaj-company.com/
- **Deploy** : Railway (auto-deploy depuis `main`)

## Cible
- Architectes DPLG / DE-HMONP
- Architectes d'intérieur
- Maîtres d'œuvre
- Bureaux d'études structure (BET)
- **Géo** : France entière, priorité Île-de-France / grandes agglomérations

## Pain points spécifiques architectes
- Délais de livraison trop courts
- Complexité réglementaire croissante (RE2020, accessibilité)
- Concurrence des logiciels low-cost / étrangers
- Besoin de différenciation par l'innovation
- Manque de temps pour se former à la tech

## Différenciation
- **Angle** : "L'IA comme levier compétitif" (gagner des appels d'offres, réduire délais)
- **Ton** : plus corporate/innovation que dentaire (secteur moins "soin", plus "business")
- **Créatifs suggérés** :
  - "Dessinez 3 variantes en 20 min avec l'IA"
  - "Comment j'ai gagné un marché public grâce à l'IA"
  - "RE2020 + IA = conformité en un clic"

## Marque
Sous-marque Kelaj — partage le même pixel (3934981656760487) avec `content_category: "architecture"`.

## Tracking Meta (validé ✓)
- **Pixel ID** : 3934981656760487 (nom : "SITE KELAJ FORMATION")
- **Compte publicitaire** : Kelaj Pub — `act_1137566528021209`
- **content_category** : `architecture` (injecté dans chaque event via `src/lib/tracking.ts`)
- **Events trackés** :
  - `PageView` — sur chargement initial + changement de route (SPA)
  - `LeadSubmitted` — sur soumission du formulaire de contact (`/FormulaireDemande`)
  - `AddPaymentInfo` — sur page paiement (`/Paiement`)
- **Dernier event reçu par Meta** : 2026-06-02 14:16 (pixel actif)
- **Vérification déployée** : `index.html` contient bien `fbq('track', 'PageView', { content_category: 'architecture' })`

## Stratégie Meta (esquisse)
- **TOFU** : Vidéos "L'IA change l'architecture" — témoignages d'architectes early adopters
- **MOFU** : Webinar / démo "IA appliquée à un projet réel"
- **BOFU** : Offre "Audit IA de votre workflow" — lead magnet premium

## Identifiants
- **Pixel** : 3934981656760487 (partagé Kelaj)
- **Page FB** : kelajformation.pro
- **Instagram** : @kelajformation
- **Site** : formation.kelaj-company.com

## MCP / API (config centralisée Kelaj)
- **Pipeboard MCP** : `meta-ads-pipeboard` connecté ✓
- **Token** : `pk_606e5004773d434994ddec8b4a6058c1`
- **Endpoint** : `https://meta-ads.mcp.pipeboard.co/?token=pk_606e5004773d434994ddec8b4a6058c1`
- **Transport** : HTTP (ajouté via `claude mcp add`)

## Repo
https://github.com/Kevin69007/kelaj-ia-architecture.git

## Prochaines étapes
- [x] Intégrer Meta Pixel avec `content_category: architecture`
- [x] Vérifier pixel actif en production
- [ ] Produire 2-3 vidéos témoignages architectes
- [ ] Valider cible avec Kevin
- [ ] Créer catalogue produits pour Dynamic Ads
