# Projet Brevo — Handoff

Hub d'envoi email multi-sociétés du groupe Cuspide/JAK, basé sur Brevo.
Version handoff au 5 mai 2026.

## C'est quoi ?

Un **skill Claude Code** (`/projet-brevo`) qui pilote l'envoi email transactionnel + campagnes pour
plusieurs sociétés du groupe, avec un volet **délivrabilité** (`/expert-delivrabilite-email`) qui
gère le warmup, les DNS (SPF/DKIM/DMARC), le monitoring Allegrow et la validation des listes.

L'objectif : pouvoir envoyer des emails marketing sans atterrir en spam, en partant
d'un domaine neuf, en suivant un protocole reproductible société par société.

## Structure

| Dossier / Fichier | Contenu |
|---|---|
| `skill-projet-brevo/` | Skill principal — routing par intention (envoi, contacts, campagnes, stats), config Brevo, logs |
| `skill-expert-delivrabilite-email/` | Skill délivrabilité — DNS, warmup schedules, statut mailboxes, API reference |
| `skill-strategie-commerciale-multi-canal/` | Skill stratégie — funnel, pixels, protocole commercial, gates décision |
| `PLAN-remediation-warmup-cuspide.md` | Plan 3 phases pour débloquer Cuspide |
| `CONTEXT-projet-cuspide.md` | État détaillé sous-projet 1 (Cuspide) + structure hub multi-sociétés |
| `CONTEXT-allegrow-acces.md` | Connexion Allegrow (login passwordless), URLs, limites API |
| `CONTEXT-bonnes-pratiques-dns.md` | Réflexe `dig` à appliquer avant tout warmup |
| `dmarc-parser/` | Parser + rapporteur DMARC (Python, launchd) |
| `SECRETS.env.enc` | Credentials chiffrés AES-256 (Brevo + IONOS + Allegrow) |

## Pour reprendre en local

1. Cloner ce repo
2. Copier les dossiers `skill-*` dans `~/.claude/skills/` (ou équivalent local)
3. Demander le mot de passe à Kevin pour déchiffrer `SECRETS.env.enc`
4. Lire `PLAN-remediation-warmup-cuspide.md` puis avancer Phase 1

## Contact projet

Kevin Jean — kevin.jean1@gmail.com
