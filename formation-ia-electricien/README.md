# Formation IA — Électriciens

## Produit
Formation à l'intelligence artificielle pour les électriciens et entreprises d'électricité : devis automatisés, gestion de chantier, conformité réglementaire (NFC 15-100, RE2020), prospection digitale.

## Site
- **Prod** : https://ia-expert-electriciens.kelaj-company.com/
- **Deploy** : Railway (auto-deploy depuis `main`)

## Cible
- Électriciens indépendants
- Entreprises d'électricité (PME)
- Installateurs en énergies renouvelables
- Automaticiens
- **Géo** : France entière, priorité IDF / grandes agglomérations

## Pain points spécifiques électriciens
- Temps passé sur les devis et factures (paperasse)
- Difficulté à se différencier de la concurrence low-cost
- Complexité réglementaire croissante (NFC 15-100, RE2020, primes rénov)
- Manque de temps pour se former à la tech
- Besoin d'optimiser les déplacements et planning chantiers

## Différenciation
- **Angle** : "L'IA comme levier de productivité" (gagner du temps sur les devis, augmenter le panier moyen)
- **Ton** : pragmatique, terrain, résultats rapides
- **Créatifs suggérés** :
  - "Votre devis électricité en 5 min avec l'IA"
  - "Comment j'ai gagné 10h/semaine grâce à ChatGPT"
  - "NFC 15-100 + IA = conformité sans prise de tête"

## Marque
Sous-marque Kelaj — partage le même pixel (3934981656760487) avec `content_category: "electricien"`

## Tracking Meta (intégré ✓)
- **Pixel ID** : 3934981656760487 (nom : "SITE KELAJ FORMATION")
- **Compte publicitaire** : Kelaj Pub — `act_1137566528021209`
- **content_category** : `electricien` (injecté dans chaque event via `src/lib/tracking.ts`)
- **Events trackés** :
  - `PageView` — sur chargement initial + changement de route (SPA)
  - `LeadSubmitted` — sur soumission du formulaire de contact (`/FormulaireDemande`)
  - `AddPaymentInfo` — sur page paiement (`/Paiement`)

## MCP / API (config centralisée Kelaj)
- **Pipeboard MCP** : `meta-ads-pipeboard` connecté ✓
- **Token** : `pk_606e5004773d434994ddec8b4a6058c1`
- **Endpoint** : `https://meta-ads.mcp.pipeboard.co/?token=pk_606e5004773d434994ddec8b4a6058c1`

## Repo
https://github.com/Kevin69007/kelaj-ia-electriciens.git

## Prochaines étapes
- [x] Intégrer Meta Pixel avec `content_category: electricien`
- [ ] Vérifier pixel actif en production
- [ ] Produire 2-3 vidéos témoignages électriciens
- [ ] Valider cible avec Kevin
- [ ] Créer catalogue produits pour Dynamic Ads
