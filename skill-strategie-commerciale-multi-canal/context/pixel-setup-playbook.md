# Playbook — Setup Meta Pixel & CAPI

Référence reproductible pour l'installation et la vérification des pixels Meta sur n'importe quelle société du hub. Basé sur les mises en place Cuspide et Kelaj.

## Prérequis avant setup

- [ ] Avoir le bon Pixel ID (vérifier dans Meta Events Manager)
- [ ] Avoir le bon Business Manager et Ad Account
- [ ] Vérifier que le domaine est associé au pixel dans Meta Business Suite
- [ ] Avoir les accès admin au site (WordPress ou repo Next.js)

---

## Type A — Site WordPress/WooCommerce

**Plugin recommandé :** `PixelYourSite`

### Procédure
1. Installer PixelYourSite (gratuit suffisant pour base + CAPI)
2. Renseigner le Pixel ID dans `PixelYourSite > Your Meta Pixel`
3. Activer :
   - `Enable Pixel`
   - `Enable Conversion API` + coller le token CAPI (généré dans Meta Events Manager > Paramètres > API Conversions)
   - `Enable Advanced Matching`
4. Sauvegarder
5. Vider le cache WordPress (`Flush site cache`)

### Vérification
- Ouvrir le site en navigation privée
- Extension **Meta Pixel Helper** (Chrome) → vérifier `PageView` actif
- Naviguer sur une page produit → vérifier `ViewContent`
- Meta Events Manager : "Événements de test" pour confirmer la remontée

### Événements automatiques (WooCommerce)
PixelYourSite déclenche automatiquement :
- `PageView` (toutes les pages)
- `ViewContent` (pages produits)
- `AddToCart` (ajout panier)
- `InitiateCheckout` (début paiement)
- `Purchase` (achat confirmé)

### Problèmes fréquents WordPress
- **Aucun événement ne remonte** → vérifier CookieYes/complianz ne bloque pas le pixel avant consentement
- **Token CAPI expiré** → régénérer dans Meta Events Manager > Paramètres > API Conversions
- **Plugin en conflit** → désactiver temporairement autres plugins de tracking

---

## Type B — Site Next.js / React custom

**Méthode :** Injection manuelle dans le layout + helpers de tracking

### Procédure
1. **Base pixel** — injecter dans `app/layout.jsx` (ou `_app.js`) dans `<head>` :
   ```jsx
   const fbPixelId = '3934981656760487'; // Pixel ID de la société
   ```
   Utiliser le script standard Meta (fbevents.js) avec `fbq('init', pixelId)` + `fbq('track', 'PageView')`.

2. **Helpers tracking** — créer `lib/tracking.js` :
   ```js
   export const trackMeta = (eventName, parameters = {}) => {
     if (typeof window !== "undefined" && window.fbq) {
       window.fbq("track", eventName, parameters);
     }
   };
   ```

3. **Événements personnalisés** — brancher sur les CTA et formulaires :
   ```jsx
   import { trackMeta } from "@/lib/tracking";

   const handleRdvClick = () => {
     trackMeta("Schedule", { content_name: "Prendre RDV" });
   };
   ```

4. Déployer (merge + build + deploy)

### Vérification
- Même procédure que WordPress : Meta Pixel Helper + Events Manager
- Vérifier que `typeof window !== "undefined"` protège bien le SSR

---

## Intégration Meta Business Suite — API Conversions (CAPI)

### Wizard Meta ("Connecter l'activité avec l'API Conversions")

**Étapes :**
1. Choisir **"Intégration directe"** (pas "Intégration de partenaire" — le site est custom)
2. Sélectionner les événements : `Acheter`, `LeadSubmitted`, etc.
3. **Source : choisir "Web"** (et non "Messages") pour chaque événement
4. Paramètres événements recommandés :
   - Requis : `Heure de l'évènement`, `Nom de l'évènement`, `URL de la source`, `Origine de l'action`
   - Achat : `Devise`, `Valeur`
5. Paramètres informations client (pour matching) :
   - **Email** (priorité #1)
   - **Téléphone**
   - **Prénom** / **Nom de famille**
   - **ID externe** (si user ID propre)
   - **Cookie fbc** + **Cookie fbp**
   - **Adresse IP client**
   - **Ville**, **Pays**, **Code postal**

### Post-setup
- Ne pas cliquer sur "Associer" dans l'onglet Actions si c'est un setup "1 clic sans code" — ça ne marche que pour Shopify/partenaires
- Sur site custom, le CAPI nécessite un backend qui envoie les events server-side (token + appel API Meta)

---

## Checklist post-setup (obligatoire)

| # | Vérification | Comment |
|---|-------------|---------|
| 1 | Meta Pixel Helper affiche PageView | Extension Chrome sur le site en navigation privée |
| 2 | Events Manager reçoit des événements | Onglet "Vue d'ensemble" du pixel |
| 3 | CAPI activée | Paramètres > API Conversions — statut "Activé" |
| 4 | Domaine associé | Paramètres > Domaines — le domaine apparaît |
| 5 | Page Facebook + Instagram reliées | Paramètres > Sources de données > Pixel > Pages associées |
| 6 | Pas d'erreur console | F12 > Console — pas d'erreur fbevents.js |

---

## Rappels importants multi-sociétés

- **Jamais mélanger les pixels** entre sociétés (ex: Cuspide ≠ Kelaj)
- **1 Pixel ID par domaine principal** — formations-dentaire.fr a son pixel, cuspide.fr a le sien
- **Landing page ≠ site principal** — peuvent partager le même pixel si même marque
- **WooCommerce = catalogue automatique** possible — activer pour Dynamic Ads en phase 2
