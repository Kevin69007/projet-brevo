# Projet Brevo — Handoff

Hub d'envoi email multi-sociétés du groupe Cuspide/JAK, basé sur Brevo (anciennement Sendinblue).
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
| `skill-projet-brevo/` | Le skill principal — routing par intention (envoi, contacts, campagnes, stats), config Brevo, logs |
| `skill-expert-delivrabilite-email/` | Skill délivrabilité — DNS, warmup schedules, statut mailboxes, API reference Allegrow |
| `PLAN-remediation-warmup-cuspide.md` | Plan 3 phases approuvé pour débloquer Cuspide (sous-projet bloqué) |
| `CONTEXT-projet-cuspide.md` | État détaillé sous-projet 1 (Cuspide) + structure hub multi-sociétés |
| `CONTEXT-allegrow-acces.md` | Comment se connecter à Allegrow (login passwordless), URLs, limites API |
| `CONTEXT-bonnes-pratiques-dns.md` | Réflexe `dig` à appliquer avant tout warmup |
| `SECRETS.env.enc` | Credentials chiffrés AES-256 (Brevo + IONOS + Allegrow). Mot de passe transmis séparément par Kevin |

## État actuel — sous-projet 1 (Cuspide)

**BLOQUÉ.** Warmup mailbox `contact@news.cuspide.fr` depuis le 26/03/2026.
Au 05/05 : spam rate 58.44%, reputation 41.56%. Gate <5% non atteint.

**Root cause identifié :** DKIM et DMARC absents du DNS sous-domaine `news.cuspide.fr`.
40 jours de warmup ont entraîné Gmail/Yahoo (politique 02/2024 : DKIM+DMARC obligatoires)
à classer le domaine en spam.

**À faire :** voir `PLAN-remediation-warmup-cuspide.md` — 3 phases.

## Sous-projets à venir

Chaque société du groupe aura à terme son propre sous-projet (sous-domaine + mailbox + warmup
indépendants) :
- JAK Formation, Pumpy, AS Travaux, Wei-Wei, Padelstars, etc.

Le pattern Cuspide servira de modèle (avec leçons apprises sur DNS).

## Outils & accès

- **Brevo API** : clé dans `SECRETS.env.enc` (var `BREVO_API_KEY`)
  - 11 352 contacts, 9 975 crédits, domaine news.cuspide.fr authentifié
- **IONOS DNS API** : clés dans `SECRETS.env.enc` (vars `IONOS_API_PREFIX` + `IONOS_API_SECRET`)
  - Zone cuspide.fr ID : `6a9b6398-2cf9-11ec-bda4-0a5864441f49`
  - Header HTTP : `X-API-Key: ${IONOS_API_PREFIX}.${IONOS_API_SECRET}`
- **Allegrow** : `https://app.neverspam.io` — login passwordless email `contact@jak-company.com`
  + code 6 chiffres reçu par mail. Plan AppSumo Premium, 2 500 crédits validation.
  ⚠️ **Pas d'API stats** (que validation email) — passer par le dashboard web.
- **Mailbox warmup** : IONOS Mail Basic, IMAP `imap.ionos.fr:993`, SMTP `smtp.ionos.fr:587`

## Déchiffrer les credentials

`SECRETS.env.enc` contient toutes les clés API (Brevo, IONOS, Allegrow) chiffrées en AES-256.
Mot de passe transmis séparément par Kevin (canal de ton choix : SMS, vocal, autre).

```bash
# Déchiffrer
openssl enc -aes-256-cbc -d -pbkdf2 -in SECRETS.env.enc -out brevo-secrets.env
# (saisir le mot de passe)

# Sourcer dans le shell
source brevo-secrets.env

# Vérifier
echo $BREVO_API_KEY
```

⚠️ Ne pas committer `brevo-secrets.env` une fois déchiffré. L'ajouter à `.gitignore`.

## Pour reprendre en local

1. Décompresser le zip et lire ce README
2. Demander le mot de passe à Kevin et déchiffrer `SECRETS.env.enc` (cf. ci-dessus)
3. Copier les deux dossiers `skill-*` dans `~/.claude/skills/` (ou équivalent local)
4. `source brevo-secrets.env` dans le shell où tournera Claude Code
5. Lire `PLAN-remediation-warmup-cuspide.md` puis avancer Phase 1 (DKIM IONOS)

## Contact projet
Kevin Jean — `kevin.jean1@gmail.com` / `+33 6 68 48 56 29`
