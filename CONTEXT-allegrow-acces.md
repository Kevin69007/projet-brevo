---
name: Allegrow dashboard — accès et limites API
description: URL dashboard, limites API stats (403), workflow Chrome MCP pour consulter reputation/spam rate warmup
type: reference
originSessionId: b99f8f53-147b-41ab-96a7-bc601217366f
---
# Allegrow / Neverspam — accès stats warmup

## URLs
- App : **https://app.neverspam.io** (domaine réel, pas allegrow.co)
- Login OAuth : `https://auth.allegrow.co` (redirige vers app.neverspam.io)
- Performance mailboxes (reputation/spam rate par domaine) : `https://app.neverspam.io/user/mailboxes`
- Safety Net Everywhere (validation listes CSV) : `https://app.neverspam.io/user/safety-net-everywhere/`
- Settings compte : `https://app.neverspam.io/user/settings`

## API — ce qui marche / ne marche pas

| Endpoint | Statut | Usage |
|---|---|---|
| `POST /v1/email/validate` | ✅ | Validation email synchrone |
| `POST /v1/email/validate-async` | ✅ | Validation bulk + webhook |
| `GET /v1/mailboxes`, `/v1/warmup`, `/v1/reputation`, `/v1/account`, `/v1/stats` | ❌ 403 | **N'existent pas** sur le plan AppSumo Premium |

**Conclusion : pour consulter reputation / spam rate warmup → obligatoire de passer par le dashboard web.** Aucun endpoint stats exposé même avec API key valide.

## Workflow consultation stats warmup
1. Chrome MCP (`mcp__claude-in-chrome-local__browser_navigate`) → `https://app.neverspam.io`
2. **Login passwordless** : cliquer "Sign In" → saisir email **`contact@jak-company.com`** → cliquer "Continuer" → cliquer **"Recevoir code par email"** (Allegrow envoie un code à 6 chiffres sur la boîte) → Kevin lit le code dans Gmail et le saisit dans Chrome
3. `browser_navigate` → `https://app.neverspam.io/user/mailboxes` (Performance)
4. Attendre chargement (skeleton ~2s) puis `browser_screen_capture`
5. Scroller pour voir tous les domaines + leurs courbes reputation

## Compte
- Plan : AppSumo Lifetime Premium
- Crédits validation : 2 500
- Owner : Kevin Jean — `contact@jak-company.com`
- Mailboxes connectées (au 05/05/2026) : `contact@news.cuspide.fr` (warmup), `amine@besmilecare.fr`, `contact@support.besmilecare.fr`, `kevin@mail.besmilecare.fr` (monitoring passif)

## Clé API
- Variable env : `ALLEGROW_API_KEY` (dans `~/.env.claude`)
- Header : `x-api-key: $ALLEGROW_API_KEY`
- Base URL : `https://api.allegrow.co/v1/`
- Docs : https://docs.allegrow.co/

## Pièges
- Test emails Allegrow tagués `- myNs.` ou `nsMotif.` → **ne JAMAIS y répondre manuellement** (consigne Allegrow), créer un label productivity Gmail (https://help.allegrow.co/en/articles/4645848)
- L'app indique "Connected" même si reputation s'effondre — vérifier régulièrement le dashboard, pas se fier à l'absence d'alerte
