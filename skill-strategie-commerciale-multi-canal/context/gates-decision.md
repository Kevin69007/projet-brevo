# Gates de décision — référence rapide

À chaque gate, vérifier la cible et décider d'avancer / corriger / pivoter.

## Gate J+7 — Fin Phase 1

**Cible :** tout le setup Phase 1 est en place.

| Item | Cible | Si non |
|---|---|---|
| DNS auth | `dig` confirme SPF + DKIM 3 sélecteurs + DMARC sub & parent | Bloquer warmup, corriger DNS |
| Mail-tester | >8/10 (idéal 10/10) | Identifier ce qui fait perdre des points |
| Warmup Allegrow | Démarré (mailbox connectée) | Vérifier IMAP/SMTP IONOS |
| Pixels | Installés + remontent du trafic | Réinstaller, vérifier conversions |
| Comptes sociaux | Actifs et configurés | Compléter |
| Scraping | Configuré (peut tourner) | Setup outils (Octoparse/Apify) |
| SEO plan | Audit + plan éditorial | Faire l'audit |

**Décision :** si tout OK → Phase 2. Sinon → résoudre les blockers AVANT.

## Gate J+14 — Mi-warmup

**Cible :** spam rate <20% (Allegrow)

| Réalité | Décision |
|---|---|
| <20% | ✅ Continuer Phase 2, on est sur la bonne pente |
| 20-30% | ⚠️ Surveillance accrue, vérifier rapports DMARC |
| >30% | 🚨 Audit approfondi : contenu warmup, listes Allegrow, IP partagée IONOS |

## Gate J+21 — Validation trajectoire

**Cible :** spam rate <10%

| Réalité | Décision |
|---|---|
| <10% | ✅ Trajectoire OK, on tient le rythme |
| 10-20% | ⚠️ Possible mais surveiller, prolonger warmup si besoin |
| >20% | 🚨 **Plan B activé** : nouveau sous-domaine OU bascule Brevo SMTP direct |

**Plan B Option A — Nouveau sous-domaine**
- Créer `email.<societe>.com` ou `mail.<societe>.com`
- DNS complet d'entrée
- Warmup 4 semaines from scratch
- Garde le contrôle complet de l'envoi via IONOS

**Plan B Option B — Brevo SMTP direct**
- Configurer Brevo pour envoyer depuis le sous-domaine existant
- Brevo signe avec sa propre infra DKIM/SPF
- Le sous-domaine sert juste de From-domain
- Plus rapide (pas de warmup)
- Moins de contrôle long terme

## Gate J+28 — Fin warmup nominal

**Cible :** spam rate <5%

| Réalité | Décision |
|---|---|
| <5% | ✅ Démarrer le gate 7-jours (vérifier que ça reste <5% pendant 7j consécutifs) |
| 5-10% | ⚠️ Prolonger warmup 1-2 semaines |
| >10% | 🚨 Plan B (cf. J+21) |

## Gate J+35 — Validation gate 7-jours

**Cible :** 7 jours consécutifs spam rate <5%

| Réalité | Décision |
|---|---|
| 7j ✅ | 🟢 **Première campagne email autorisée** (volume limité 200-500 contacts) |
| Cassé à J+30 par ex | Reset gate, redémarrer le compteur 7j |

## Gate J+42 — Maturité pixels

**Cible :** pixels publicitaires ont accumulé assez de data pour lookalikes

| Réalité | Décision |
|---|---|
| 100+ conversions trackées | ✅ Lookalike 1% activable |
| 50-100 conversions | ⚠️ Possible mais qualité LAL faible |
| <50 conversions | ❌ Continuer pub Bdd custom + retargeting, attendre data |

## Gate J+56 — Décision scale ou pivot

**Cible :** preuve de ROI positif sur au moins 2 canaux

| Réalité | Décision |
|---|---|
| ROI+ sur 2+ canaux | ✅ Phase 4 scale + démarrer nouvelle société en parallèle |
| ROI+ sur 1 canal | ⚠️ Doubler sur ce canal, audit pourquoi les autres marchent moins |
| ROI- partout | 🚨 Stop scaling, audit fondamental (offre ? cible ? proposition ?) |

## Cadence ongoing après Phase 4

| Cadence | Action |
|---|---|
| Quotidien | Monitoring spam rate, bounces, plaintes |
| Hebdo | Revue performances toutes campagnes |
| Bi-mensuel | Audit créatif + renouvellement |
| Mensuel | Analyse ROI par canal + ré-allocation budget |
| Trimestriel | Audit SEO complet + audit délivrabilité |
