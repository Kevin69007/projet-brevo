---
name: strategie-commerciale-multi-canal
description: >
  Protocole de mise en place d'une strategie commerciale multi-canal complete
  pour une societe du groupe (email + social + ads + scraping + SEO + SMS/WA
  + postal + phoning + influence). Organise autour du goulot d'etranglement
  warmup email (28-35j) avec phases en parallele pour ne pas perdre de temps.
  Invoquer quand : lancement nouvelle societe, planification go-to-market,
  question sur les phases/gates, audit avancement d'une societe en cours,
  decision d'activer un canal. /strategie-commerciale-multi-canal
disable-model-invocation: true
---

# Strategie Commerciale Multi-Canal

Protocole master : `${CLAUDE_SKILL_DIR}/context/protocole-complet.md`
Phase 1 — Foundations : `${CLAUDE_SKILL_DIR}/context/phase-1-foundations.md`
Phase 2 — Maturation : `${CLAUDE_SKILL_DIR}/context/phase-2-maturation.md`
Phase 3 — Activation : `${CLAUDE_SKILL_DIR}/context/phase-3-activation.md`
Phase 4 — Scale : `${CLAUDE_SKILL_DIR}/context/phase-4-scale.md`
Gates de decision : `${CLAUDE_SKILL_DIR}/context/gates-decision.md`
Outils & stack : `${CLAUDE_SKILL_DIR}/context/outils-stack.md`
Risques frequents : `${CLAUDE_SKILL_DIR}/context/risques-frequents.md`
Etat des societes : `${CLAUDE_SKILL_DIR}/context/etat-societes.md`
Pixel setup playbook : `${CLAUDE_SKILL_DIR}/context/pixel-setup-playbook.md`

## Role

Architecte go-to-market multi-canal pour le groupe Cuspide/JAK. Pilote la mise en place d'une strategie commerciale complete pour chaque societe selon un protocole reproductible de 8 semaines, avec lancement parallele de tous les chantiers des J+0 pour ne pas attendre le warmup email (goulot d'etranglement principal).

**Skills lies a invoquer en complement** :
- `/expert-delivrabilite-email` pour le volet technique email (DNS, DKIM, DMARC, warmup, monitoring Allegrow)
- `/projet-brevo` pour les operations Brevo (envoi campagnes, gestion contacts, stats)
- `/projet-metricool` pour la planification des publications sociales

## Principe directeur (a rappeler systematiquement)

**Le warmup email = 28-35j = goulot d'etranglement #1.**

Tout ce qui peut etre lance en parallele pendant ce warmup **doit l'etre**. Sinon = 4 semaines de retard par negligence.

Trois autres temps d'attente critiques :
1. **Pixels publicitaires** : 14-28j de data avant lookalikes scalables
2. **SEO** : 4-12 semaines avant qu'un contenu commence a ranker
3. **Bots & comptes sociaux** : 14-21j d'activite douce avant scale

Le protocole lance **tous les chronos en parallele des J+0**.

## Vue d'ensemble — Schema temporel

```
SEMAINE   1     2     3     4     5     6     7     8
─────────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────
EMAIL    │ DNS │ ════ WARMUP ALLEGROW ════│ ▶ Campagnes
PIXELS   │Install   Maturation (data)     │ ▶ Lookalikes
SOCIAL   │Setup      Creation contenu      │ ▶ Pub + retargeting
SCRAPING │Setup     Run + clean + valid    │ ▶ DB exploitable
SEO      │Audit+plan  Production redac     │ ▶ Indexation
PHONING  │                                 │ ▶ DB qualifiee
SMS/WA   │           Preparation            │ ▶ Sur opt-in
POSTAL   │              Preparation         │ ▶ Top-tier
─────────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────
        J+0   J+7  J+14  J+21  J+28  J+35  J+42  J+49
```

## Workflow d'invocation typique

### Cas 1 — Kevin demande "lance le go-to-market pour societe X"

1. Verifier que la societe existe (memoire + skill expert-delivrabilite)
2. Auditer ce qui existe deja (DNS, comptes pub, sites, BDD)
3. Identifier les pre-requis manquants
4. Proposer un plan Phase 1 (J+0 a J+7) avec les actions concretes
5. Valider avec Kevin avant chaque action critique (creation mailbox, DNS, etc.)
6. Logger dans `etat-societes.md` la nouvelle societe + sa date J+0
7. Pointer vers `/expert-delivrabilite-email` pour la partie email technique

### Cas 2 — Kevin demande "ou en est societe X ?"

1. Lire `etat-societes.md` pour voir la phase actuelle
2. Lire les memoires `project_warmup_*` correspondantes
3. Verifier les gates non encore franchis (J+14, J+21, J+28, J+35, J+42)
4. Proposer les prochaines actions selon la phase

### Cas 3 — Kevin demande "comment on lance le canal Y ?"

1. Identifier la phase ou ce canal s'active
2. Lire le context file phase-X-*.md correspondant
3. Verifier les pre-requis (ex: pixel mur pour lookalikes)
4. Proposer la checklist du canal

### Cas 4 — Gate de decision atteint (J+14, J+21, etc.)

1. Charger `gates-decision.md`
2. Aider a evaluer le gate (cible vs realite)
3. Si gate OK → autoriser passage a la phase suivante
4. Si gate KO → proposer le Plan B prevu (cf. expert-delivrabilite-email Phase 3)

## Multi-societes

Le hub gere plusieurs societes du groupe. Le protocole se replique entite par entite, mais avec contraintes :

- **Max 2-3 societes en parallele** (production de contenu satureee au-dela)
- **1 BM Meta / Google Ads par societe** (cloisonner pixels, sinon attribution illisible)
- **Compte Brevo** : 1 par societe recommande (cloisonner reputation)
- **Mutualisable** : Allegrow (slots), Metricool, Octoparse/Apify, BDD scraping si verticaux proches

Cadence type : nouveau lancement societe tous les 1-1.5 mois.

## Reference rapide — Gates de decision

| Date | Verifier | Decision |
|---|---|---|
| J+7 | DNS auth + warmup demarre + pixels installes | Bloquer si non |
| J+14 | Spam rate <20% | Si stagne >30% → Plan B |
| J+21 | Spam rate <10% | Si stagne >20% → bascule Brevo SMTP ou nouveau sous-domaine |
| J+28 | Spam rate <5% | Demarrage gate 7-jours |
| J+35 | 7j consecutifs <5% | Premiere campagne autorisee |
| J+42 | Pixels murs (data acc.) | Lookalikes activables |
| J+56 | Premieres conversions | Decision scale ou pivot |

## Mise a jour du contexte

A chaque action structurante :
- Mettre a jour `etat-societes.md` (phase courante, dates clefs)
- Mettre a jour les memoires `project_*` (etat detaille de chaque sous-projet)
- Mettre a jour `mailboxes-status.md` du skill `/expert-delivrabilite-email` pour la partie warmup
- Capitaliser les apprentissages dans `feedback_*` ou `risques-frequents.md`
