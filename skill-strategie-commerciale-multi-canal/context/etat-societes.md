# État des sociétés du groupe — Suivi go-to-market

> Source de vérité unique pour savoir où en est chaque société dans le protocole.
> À mettre à jour à chaque action structurante.
> Dernière mise à jour : 7 mai 2026

## Légende phases

| Phase | Plage | Description |
|---|---|---|
| 0 | Pré-lancement | Pas encore démarré, en planning |
| 1 | J+0 → J+7 | Foundations |
| 2 | J+7 → J+28 | Maturation + production |
| 3 | J+28 → J+42 | Activation contrôlée |
| 4 | J+42+ | Scale & optimisation |

## Sociétés actives

### 🟢 Cuspide
- **Domaine envoi** : news.cuspide.fr
- **Mailbox warmup** : contact@news.cuspide.fr
- **J+0** : 05/05/2026 (post-fix DNS, reset baseline)
- **Phase actuelle** : Phase 2 (maturation, J+13)
- **Évolution Allegrow** :
  - 05/05 : reputation 41.56% / spam rate 58.44% (baseline post-fix)
  - 18/05 : reputation 51.00% / spam rate 49.00% (-9.4 pts en 13j)
- **Prochains gates (recalés J+21)** :
  - J+21 = 26/05/2026 (cible <20% spam)
  - J+28 = 02/06/2026 (cible <10%)
  - J+35 = 09/06/2026 (cible <5% gate démarre)
  - J+42 = 16/06/2026 (gate 7j → 1ère campagne)
- **Mailbox DMARC** : dmarc@cuspide.fr
- **Compte Brevo** : authentifié (11 352 contacts)
- **Notes** : Mail-tester 10/10 le 05/05. DMARC 98.6% PASS. Tendance positive mais gates J+14 initiaux trop agressifs — recalés J+21.

### 🟢 Kelaj Formation
- **Domaine envoi** : pros.kelaj-company.com
- **Mailbox warmup** : contact@pros.kelaj-company.com
- **From-name** : L'équipe Kelaj Formation
- **J+0** : 07/05/2026
- **Phase actuelle** : Phase 2 (maturation, J+11)
- **Évolution Allegrow** :
  - 18/05 : reputation 50.00% / spam rate 50.00% (courbe en hausse constante depuis J+0)
- **Prochains gates (recalés J+21)** :
  - J+21 = 28/05/2026 (cible <20% spam)
  - J+28 = 04/06/2026 (cible <10%)
  - J+35 = 11/06/2026 (cible <5% gate démarre)
  - J+42 = 18/06/2026 (gate 7j → 1ère campagne)
- **Mailbox DMARC** : dmarc@kelaj-company.com
- **Brevo** : Domaine `kelaj-company.com` authentifié le 18/05 (fix DKIM mismatch `partenariat.wei-wei.fr`)
- **Notes** : Mail-tester 10/10 le 07/05. DMARC 100% PASS sur `pros.kelaj-company.com`. Backscatterer = faux positif IP IONOS, ignoré. Tendance positive mais gates J+14 initiaux trop agressifs — recalés J+21.

## Sociétés en pré-lancement (Phase 0 — pas encore démarrées)

| Société | Domaine prévu | Vertical | Notes |
|---|---|---|---|
| JAK Formation | jak-company.com | Formation | À planifier |
| Pumpy | (à déterminer) | (à déterminer) | À planifier |
| AS Travaux | (à déterminer) | Travaux/BTP | À planifier |
| Wei-Wei | wei-wei.fr (anciennement carbonisé) | (à déterminer) | Quarantaine, à reconstruire éventuellement sur nouveau sous-domaine |
| Padelstars | padel-stars.fr | Sport / Padel | À planifier |
| BeSmileCare | besmilecare.fr (anciennement carbonisé) | Soins dentaires | Monitoring passif, à reconstruire si pertinent |

## Sociétés en quarantaine / archivées

- **jak-company.com** mailbox : supprimée d'Allegrow le 25/03/2026 (config issue, domaine plus utilisé)
- **partenariat.wei-wei.fr** mailbox : supprimée d'Allegrow le 25/03/2026 (carbonisée 56% spam)

## Cadence de lancement recommandée

À partir d'aujourd'hui (07/05/2026) :
- M0 (mai 2026) : Cuspide + Kelaj en cours (Phase 2)
- M1 (juin 2026) : Cuspide + Kelaj en Phase 3-4. Possibilité d'ajouter une 3ème société (JAK ou Padelstars).
- M2 (juillet 2026) : nouvelle société en Phase 1, les autres en cadence régulière
- Cible : nouvelle société en Phase 1 tous les 1-1.5 mois

## Slots Allegrow

- 2 slots libérés (jak + wei-wei suppression mars 2026)
- **1 slot consommé** par Cuspide (depuis 26/03)
- **1 slot consommé** par Kelaj (depuis 07/05)
- Slots restants dépendent du plan AppSumo Premium (vérifier capacité)
