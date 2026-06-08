# Formation IA — Chauffagistes

## Produit
Formation a l'intelligence artificielle pour le secteur du chauffage et de la plomberie : gestion de chantier, devis automatises, maintenance predictive, conformite reglementaire (RE2020, RT2012).

## Site
- **Prod** : https://ia-expert-chauffagistes.kelaj-company.com/
- **Deploy** : Railway (auto-deploy depuis `main`)

## Cible
- Chauffagistes independants
- Entreprises de chauffage / plomberie (PME)
- Installateurs thermiciens
- **Geo** : France entiere, priorite IDF / grandes agglomerations

## Pain points specifiques chauffagistes
- Temps passes sur les devis et factures (paperasse)
- Difficulte a se differencier de la concurrence low-cost
- Complexite reglementaire croissante (RE2020, primes renov, MaPrimeRenov)
- Manque de temps pour se former a la tech
- Besoin d'optimiser les deplacements et planning chantiers

## Differentiation
- **Angle** : "L'IA comme levier de productivite" (gagner du temps sur les devis, augmenter le panier moyen)
- **Ton** : pragmatique, terrain, resultats rapides
- **Creatifs suggeres** :
  - "Votre devis chauffage en 5 min avec l'IA"
  - "Comment j'ai gagne 10h/semaine grace a ChatGPT"
  - "RE2020 + IA = conformite sans prise de tete"

## Marque
Sous-marque Kelaj — partage le meme pixel (3934981656760487) avec `content_category: "chauffagiste"`

## Tracking Meta (integre ✓)
- **Pixel ID** : 3934981656760487 (nom : "SITE KELAJ FORMATION")
- **Compte publicitaire** : Kelaj Pub — `act_1137566528021209`
- **content_category** : `chauffagiste` (injecte dans chaque event via `src/lib/tracking.ts`)
- **Events trackes** :
  - `PageView` — sur chargement initial + changement de route (SPA)
  - `LeadSubmitted` — sur soumission du formulaire de contact (`/FormulaireDemande`)
  - `AddPaymentInfo` — sur page paiement (`/Paiement`)

## MCP / API (config centralisee Kelaj)
- **Pipeboard MCP** : `meta-ads-pipeboard` connecte ✓
- **Token** : `pk_606e5004773d434994ddec8b4a6058c1`
- **Endpoint** : `https://meta-ads.mcp.pipeboard.co/?token=pk_606e5004773d434994ddec8b4a6058c1`

## Repo
https://github.com/Kevin69007/kelaj-ia-chauffagiste.git

## Prochaines etapes
- [x] Integrer Meta Pixel avec `content_category: chauffagiste`
- [ ] Verifier URL de production deployee
- [ ] Produire 2-3 videos temoignages chauffagistes
- [ ] Valider cible avec Kevin
- [ ] Creer catalogue produits pour Dynamic Ads
