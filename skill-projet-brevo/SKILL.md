---
name: projet-brevo
description: >
  Hub opérationnel email Brevo (Cuspide) : envoyer emails, gérer contacts/listes,
  créer campagnes, suivre analytics. Invoquer avec /projet-brevo.
disable-model-invocation: true
---

# Brevo — Email Hub (Cuspide)

Config : `${CLAUDE_SKILL_DIR}/context/config/brevo-config.md`
Log : `${CLAUDE_SKILL_DIR}/context/memory/campaigns-log.md`

## Stack & outils
- **Brevo API directe** — `curl -H "api-key: ${BREVO_API_KEY}" https://api.brevo.com/v3/...` (mode principal)
  - Cle API : `claude-email` (xkeysib-...) dans `~/.env.claude` — Active, 9975 credits
  - Compte : Cuspide | 11 352 contacts
- **IONOS DNS API** — `curl -H "X-API-Key: ${IONOS_API_PREFIX}.${IONOS_API_SECRET}" https://api.hosting.ionos.com/dns/v1/...`
  - Cle API : `claude-dns` dans `~/.env.claude`
  - Zone cuspide.fr ID : `6a9b6398-2cf9-11ec-bda4-0a5864441f49`
- **n8n MCP** (`mcp__f2f28fa1`) — workflows Brevo existants (backup)
- **Expert strategie** : `/expert-brevo-lemlist-email-marketing` — strategie, RGPD
- **Expert delivrabilite** : `/expert-delivrabilite-email` — DNS, warmup, pre-send gate

## Routing par intention

| Input | Mode |
|-------|------|
| "envoyer", "email", destinataire + sujet | → MODE SEND |
| "contact", "ajouter", "liste", "segment" | → MODE CONTACTS |
| "campagne", "newsletter", "créer campagne" | → MODE CAMPAIGN |
| "template", "modèle" | → MODE TEMPLATES |
| "stats", "analytics", "taux d'ouverture" | → MODE ANALYTICS |
| "n8n", "workflow", "automatisation" | → MODE N8N |
| "setup", "configurer", "premier lancement" | → MODE SETUP |
| "delivrabilite", "spam", "reputation", "warmup", "DNS" | → `/expert-delivrabilite-email` |
| Aucune intention claire | Demander |

---

## MODE SEND — Email transactionnel / one-shot

1. ToolSearch `brevo` pour charger les outils d'envoi
2. Lire `brevo-config.md` pour sender par défaut
3. Paramètres : `to`, `subject`, `htmlContent` ou `templateId`
4. **Confirmer avant envoi** — afficher récapitulatif complet
5. Envoyer via MCP

---

## MODE CONTACTS

| Action | Outil MCP |
|--------|-----------|
| Ajouter/modifier contact | `create_or_update_contact` |
| Lister les listes | `get_lists` |
| Ajouter à une liste | `add_contact_to_list` |
| Voir un contact | `get_contact_info` |
| Supprimer contact | Confirmer 2x avant |

Charger `brevo-config.md` pour les IDs de listes Cuspide.

---

## MODE CAMPAIGN

1. Lire `brevo-config.md` (sender, liste cible par défaut)
2. `create_email_campaign` : name, subject, sender, recipients
3. Si template existant → `templateId`, sinon `htmlContent`
4. **NE JAMAIS envoyer directement** — créer en DRAFT
5. Fournir lien prévisualisation
6. Kevin confirme → `send_campaign` ou `schedule_campaign`
7. Logger dans `campaigns-log.md`

---

## MODE TEMPLATES

- `get_smtp_templates` — lister templates existants
- `get_smtp_template` — voir détails d'un template
- `create_smtp_template` — créer nouveau template
- `update_smtp_template` — modifier existant

---

## MODE ANALYTICS

- `get_email_campaign_stats` — stats d'une campagne spécifique
- Vue globale : lister campagnes récentes + stats
- Output en tableau markdown :

| Métrique | Valeur | Benchmark |
|----------|--------|-----------|
| Taux ouverture | X% | 20-25% |
| Taux clic | X% | 2-5% |
| Bounce | X% | <2% |
| Désinscription | X% | <0.5% |

Pour analyse stratégique → invoquer `/expert-brevo-lemlist-email-marketing`

---

## MODE N8N

- ToolSearch `search_workflows` pour trouver workflows Brevo existants
- `execute_workflow` pour déclencher manuellement
- Référencer dans `campaigns-log.md` après exécution

---

## GATE DELIVRABILITE (obligatoire avant tout envoi campagne/outreach)

Avant MODE SEND (campagne) ou cold outreach :
1. Lire `expert-delivrabilite-email/context/mailboxes-status.md` → verifier spam rate < 5%
2. Si liste > 50 contacts → valider via EmailListValidation (API dans api-reference.md)
3. Verifier DNS (SPF/DKIM/DMARC) du sous-domaine emetteur
4. Si un check echoue → **BLOQUER l'envoi**, expliquer pourquoi, proposer correction

Pour toute question delivrabilite → invoquer `/expert-delivrabilite-email`

---

## Regles

1. **Confirmation obligatoire** avant tout envoi (email ou campagne)
2. **Brevo API directe** (cle `claude-email`) — mode principal. n8n bridge en backup
3. **Campagnes en DRAFT** — jamais d'envoi direct sans validation Kevin
4. Sender par defaut depuis `brevo-config.md` (ne pas hardcoder)
5. **Gate delivrabilite** avant tout envoi campagne (voir section ci-dessus)
6. Pour strategie/RGPD → `/expert-brevo-lemlist-email-marketing`
7. Pour delivrabilite/DNS/warmup → `/expert-delivrabilite-email`
8. Logger campagnes importantes dans `campaigns-log.md`
9. **RGPD** : verifier consentement avant ajout contacts

## MODE SETUP — Premier lancement / configuration

1. Verifier `brevo-config.md` — si `XXX` presents :
   - `curl -H "api-key: ${BREVO_API_KEY}" https://api.brevo.com/v3/contacts/lists` → remplir IDs listes
   - `curl -H "api-key: ${BREVO_API_KEY}" https://api.brevo.com/v3/smtp/templates` → remplir IDs templates
   - `curl -H "api-key: ${BREVO_API_KEY}" https://api.brevo.com/v3/senders/domains` → verifier domaines
2. Invoquer `/expert-delivrabilite-email` pour audit DNS
3. Envoyer email test a kevin.jean1@gmail.com
4. Verifier score sur mail-tester.com
