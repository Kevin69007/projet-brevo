# Formation IA — Gestion de patrimoine

## Produit
Formation à l'intelligence artificielle pour les conseillers en gestion de patrimoine (CGP) et cabinets de conseil : analyse de portefeuille, reporting client automatisé, conformité réglementaire, prospection digitale.

## Site
- **Prod** : https://ia-expert-gestion-patrimoine.kelaj-company.com/
- **Deploy** : Railway (auto-deploy depuis `main`)

## Cible
- Conseillers en gestion de patrimoine (CGP)
- Gérants indépendants de patrimoine
- Conseillers financiers
- Cabinets de conseil en gestion de patrimoine
- **Géo** : France entière, priorité IDF / grandes métropoles régionales

## Pain points spécifiques CGP
- Temps passé sur le reporting et la documentation client
- Difficulté à personnaliser les recommandations à grande échelle
- Conformité réglementaire croissante (MiFID II, RGPD, obligations fiscales)
- Prospection digitale inexistante ou inefficace
- Manque de temps pour se former à la tech

## Différenciation
- **Angle** : "L'IA comme multiplicateur de conseil" (gain de temps sur le reporting, personnalisation des recommandations)
- **Ton** : professionnel, rassurant, expert
- **Créatifs suggérés** :
  - "Votre rapport patrimonial en 10 min avec l'IA"
  - "Comment j'ai doublé mon portefeuille client grâce au digital"
  - "IA + Patrimoine = conseil personnalisé à l'échelle"

## Marque
Sous-marque Kelaj — partage le même pixel (3934981656760487) avec `content_category: "gestion-patrimoine"`

## Tracking Meta (intégré ✓)
- **Pixel ID** : 3934981656760487 (nom : "SITE KELAJ FORMATION")
- **Compte publicitaire** : Kelaj Pub — `act_1137566528021209`
- **content_category** : `gestion-patrimoine` (injecté dans chaque event via `src/lib/tracking.ts`)
- **Events trackés** :
  - `PageView` — sur chargement initial + changement de route (SPA)
  - `LeadSubmitted` — sur soumission du formulaire de contact (`/FormulaireDemande`)
  - `AddPaymentInfo` — sur page paiement (`/Paiement`)

## MCP / API (config centralisée Kelaj)
- **Pipeboard MCP** : `meta-ads-pipeboard` connecté ✓
- **Token** : `pk_606e5004773d434994ddec8b4a6058c1`
- **Endpoint** : `https://meta-ads.mcp.pipeboard.co/?token=pk_606e5004773d434994ddec8b4a6058c1`

## Repo
https://github.com/Kevin69007/kelaj-ia-gestionpatrimoine.git

## Prochaines étapes
- [x] Intégrer Meta Pixel avec `content_category: gestion-patrimoine`
- [ ] Vérifier pixel actif en production
- [ ] Produire 2-3 vidéos témoignages CGP
- [ ] Valider cible avec Kevin
- [ ] Créer catalogue produits pour Dynamic Ads
