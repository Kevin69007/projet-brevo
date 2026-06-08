# Formation IA — Coachs sportifs

## Produit
Formation à l'intelligence artificielle pour les coachs sportifs : programmation personnalisée, analyse de performance, nutrition, gestion clientèle, automatisation des tâches administratives.

## Site
- **Prod** : https://ia-expert-coachs-sportifs.kelaj-company.com/
- **Deploy** : Railway (auto-deploy depuis `main`)

## Cible
- Coachs sportifs indépendants
- Entraîneurs personnels (personal trainers)
- Préparateurs physiques
- Gérants de salles de sport / box
- **Géo** : France entière, priorité IDF / grandes agglomérations

## Pain points spécifiques coachs sportifs
- Temps passé sur la programmation et planification des séances
- Difficulté à se différencier dans un marché saturé
- Gestion administrative chronophage (rdv, factures, suivi client)
- Besoin de personalisation à grande échelle
- Manque de temps pour se former à la tech

## Différenciation
- **Angle** : "L'IA comme bras droit du coach" (programmation auto, suivi personnalisé, gain de temps)
- **Ton** : énergique, résultats, communauté
- **Créatifs suggérés** :
  - "Votre programme client en 2 min avec l'IA"
  - "Comment j'ai doublé mon nombre de clients grâce à ChatGPT"
  - "IA + Coaching = résultats x3 sans travailler plus"

## Marque
Sous-marque Kelaj — partage le même pixel (3934981656760487) avec `content_category: "coach-sportif"`

## Tracking Meta (intégré ✓)
- **Pixel ID** : 3934981656760487 (nom : "SITE KELAJ FORMATION")
- **Compte publicitaire** : Kelaj Pub — `act_1137566528021209`
- **content_category** : `coach-sportif` (injecté dans chaque event via `src/lib/tracking.ts`)
- **Events trackés** :
  - `PageView` — sur chargement initial + changement de route (SPA)
  - `LeadSubmitted` — sur soumission du formulaire de contact (`/FormulaireDemande`)
  - `AddPaymentInfo` — sur page paiement (`/Paiement`)

## MCP / API (config centralisée Kelaj)
- **Pipeboard MCP** : `meta-ads-pipeboard` connecté ✓
- **Token** : `pk_606e5004773d434994ddec8b4a6058c1`
- **Endpoint** : `https://meta-ads.mcp.pipeboard.co/?token=pk_606e5004773d434994ddec8b4a6058c1`

## Repo
https://github.com/Kevin69007/kelaj-ia-coachsportif.git

## Prochaines étapes
- [x] Intégrer Meta Pixel avec `content_category: coach-sportif`
- [ ] Vérifier pixel actif en production
- [ ] Produire 2-3 vidéos témoignages coachs sportifs
- [ ] Valider cible avec Kevin
- [ ] Créer catalogue produits pour Dynamic Ads
