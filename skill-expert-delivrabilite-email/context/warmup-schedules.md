# Warmup Schedules — Par Mailbox

> Calendrier a demarrer apres Phase 0 (quarantaine + DNS fixes)

## Schedule type — Mailbox recuperable (spam 30-40%)

Recovery mode : volume tres bas, patience.

| Semaine | Volume/jour | Type d'envoi | Objectif spam rate |
|---------|------------|-------------|-------------------|
| S1-2 | 5-10 | Warmup network Allegrow uniquement | < 25% |
| S3-4 | 15-20 | Warmup + emails internes equipe | < 15% |
| S5-6 | 30-50 | Petits segments opt-in connus | < 10% |
| S7-8 | 50-100 | Segments elargis, monitores daily | < 5% |

**Gate** : spam < 5% pendant 7 jours consecutifs → cold outreach autorise.

## Schedule type — Nouvelle mailbox (from zero)

| Semaine | Volume/jour | Type d'envoi |
|---------|------------|-------------|
| S1 | 5 | Warmup network uniquement |
| S2 | 10-15 | Warmup network |
| S3 | 20-30 | Warmup + internes |
| S4 | 50 | Petits segments opt-in |
| S5+ | 100+ | Progressive ramp-up |

## Suivi par mailbox

### amine@besmilecare.fr
- Debut warmup : A DEMARRER apres quarantaine
- Schedule : Recovery (spam actuel 35.71%)
- Check weekly dans Allegrow

### kevin@mail.besmilecare.fr
- Debut warmup : A DEMARRER apres quarantaine
- Schedule : Recovery (spam actuel 39.76%)
- Check weekly dans Allegrow

### contact@partenariat.wei-wei.fr
- **QUARANTAINE** — spam 68.82%
- Decision : creer nouveau sous-domaine OU attendre 4-6 semaines

### contact@support.besmilecare.fr
- **QUARANTAINE** — spam 66.75%
- Decision : creer nouveau sous-domaine OU attendre 4-6 semaines

### contact@jak-company.com
- **BLOQUE** — config issue dans Allegrow
- Etape 1 : fixer DNS
- Etape 2 : warmup from zero
