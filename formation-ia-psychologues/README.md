# Formation IA Psychologues — Meta Pixel

## Site
- **URL** : https://ia-expert-psychologues.kelaj-company.com/
- **Déploiement** : Railway (auto-deploy depuis `main`)

## Meta Pixel
- **Pixel ID** : `3934981656760487`
- **content_category** : `psychologues`

## Événements trackés

| Événement | Déclencheur | Fichier |
|-----------|-------------|---------|
| `PageView` | Chaque changement de route SPA | `src/App.tsx` (PageViewTracker) |
| `PageView` | Chargement initial | `index.html` (pixel base) |
| `LeadSubmitted` | Soumission formulaire de contact | `src/components/ContactFormulaire.tsx` |
| `AddPaymentInfo` | Remplissage infos paiement | `src/pages/Paiement.tsx` |

## Stack
- Vite + React + TypeScript
- React Router SPA
- TailwindCSS + shadcn/ui

## Intégration
Le pixel est injecté dans `index.html` et les événements SPA sont gérés via `src/lib/tracking.ts`.
