# Formation IA — Couvreurs

## Produit
Formation à l'intelligence artificielle pour les couvreurs et entreprises de couverture : devis automatisés, gestion de chantier, conformité réglementaire (RE2020, RT2012), prospection digitale.

## Site
- **Prod** : https://ia-expert-couvreurs.kelaj-company.com/
- **Deploy** : Railway (auto-deploy depuis `main`)

## Cible
- Couvreurs indépendants
- Entreprises de couverture (PME)
- Charpentiers-couvreurs
- Zingueurs
- **Géo** : France entière, priorité IDF / grandes agglomérations

## Pain points spécifiques couvreurs
- Temps passé sur les devis et factures (paperasse)
- Difficulté à se différencier de la concurrence low-cost
- Complexité réglementaire croissante (RE2020, primes rénov, MaPrimeRenov)
- Manque de temps pour se former à la tech
- Besoin d'optimiser les déplacements et planning chantiers

## Différenciation
- **Angle** : "L'IA comme levier de productivité" (gagner du temps sur les devis, augmenter le panier moyen)
- **Ton** : pragmatique, terrain, résultats rapides
- **Créatifs suggérés** :
  - "Votre devis couverture en 5 min avec l'IA"
  - "Comment j'ai gagné 10h/semaine grâce à ChatGPT"
  - "RE2020 + IA = conformité sans prise de tête"

## Marque
Sous-marque Kelaj — partage le même pixel (3934981656760487) avec `content_category: "couvreur"`

## Tracking Meta (intégré ✓)
- **Pixel ID** : 3934981656760487 (nom : "SITE KELAJ FORMATION")
- **Compte publicitaire** : Kelaj Pub — `act_1137566528021209`
- **content_category** : `couvreur` (injecté dans chaque event via `src/lib/tracking.ts`)
- **Events trackés** :
  - `PageView` — sur chargement initial + changement de route (SPA)
  - `LeadSubmitted` — sur soumission du formulaire de contact (`/FormulaireDemande`)
  - `AddPaymentInfo` — sur page paiement (`/Paiement`)

## MCP / API (config centralisée Kelaj)
- **Pipeboard MCP** : `meta-ads-pipeboard` connecté ✓
- **Token** : `pk_606e5004773d434994ddec8b4a6058c1`
- **Endpoint** : `https://meta-ads.mcp.pipeboard.co/?token=pk_606e5004773d434994ddec8b4a6058c1`

## Repo
https://github.com/Kevin69007/kelaj-ia-couvreurs.git

## Prochaines étapes
- [x] Intégrer Meta Pixel avec `content_category: couvreur`
- [ ] Vérifier pixel actif en production
- [ ] Produire 2-3 vidéos témoignages couvreurs
- [ ] Valider cible avec Kevin
- [ ] Créer catalogue produits pour Dynamic Ads
