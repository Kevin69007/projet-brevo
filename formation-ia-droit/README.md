# Formation IA — Droit

## Produit
Formation a l'intelligence artificielle pour les professionnels du droit : analyse documentaire, redaction automatisee de contrats, veille juridique, conformite RGPD, assistance client.

## Site
- **Prod** : https://ia-droit.kelaj-company.com/
- **Deploy** : Railway (auto-deploy depuis `main`)

## Cible
- Avocats independants et cabinets d'avocats
- Conseillers juridiques
- Juristes d'entreprise
- Notaires
- Experts-comptables avec activite juridique
- **Geo** : France entiere, priorite IDF / grandes metropoles regionales

## Pain points specifiques professionnels du droit
- Temps passe sur la redaction et l'analyse de documents repetitifs
- Difficulte a suivre l'evolution legislative
- Besoin d'automatiser les taches a faible valeur ajoutee
- Conformite croissante (RGPD, reglementations sectorielles)
- Manque de temps pour se former a la tech

## Differentiation
- **Angle** : "L'IA comme associe numerique" (gagner du temps sur la redaction, ameliorer la precision)
- **Ton** : professionnel, rigoureux, innovant
- **Creatifs suggeres** :
  - "Votre contrat en 10 min avec l'IA"
  - "Comment j'ai reduit mes heures de redaction de moitie"
  - "IA + Droit = conseil plus rapide, plus juste"

## Marque
Sous-marque Kelaj — partage le meme pixel (3934981656760487) avec `content_category: "droit"`

## Tracking Meta (integre ✓)
- **Pixel ID** : 3934981656760487 (nom : "SITE KELAJ FORMATION")
- **Compte publicitaire** : Kelaj Pub — `act_1137566528021209`
- **content_category** : `droit` (injecte dans chaque event via `src/lib/tracking.ts`)
- **Events trackes** :
  - `PageView` — sur chargement initial + changement de route (SPA)
  - `LeadSubmitted` — sur soumission du formulaire de contact (`/FormulaireDemande`)
  - `AddPaymentInfo` — sur page paiement (`/Paiement`)

## MCP / API (config centralisee Kelaj)
- **Pipeboard MCP** : `meta-ads-pipeboard` connecte ✓
- **Token** : `pk_606e5004773d434994ddec8b4a6058c1`
- **Endpoint** : `https://meta-ads.mcp.pipeboard.co/?token=pk_606e5004773d434994ddec8b4a6058c1`

## Repo
https://github.com/Kevin69007/kelaj-ia-droit.git

## Prochaines etapes
- [x] Integrer Meta Pixel avec `content_category: droit`
- [ ] Verifier pixel actif en production
- [ ] Produire 2-3 videos temoignages avocats/juristes
- [ ] Valider cible avec Kevin
- [ ] Creer catalogue produits pour Dynamic Ads
