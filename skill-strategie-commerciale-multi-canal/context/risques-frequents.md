# Risques fréquents & comment les éviter

Capitalisation des leçons apprises sur les sous-projets précédents.

## Email & délivrabilité

| Risque | Cause racine | Mitigation |
|---|---|---|
| Croire un bilan "DNS OK" sans audit | Confiance aveugle au texte rédigé par d'autres | **Toujours `dig` avant warmup** (leçon Cuspide 40j perdus) |
| Envoyer une campagne avant gate <5% | Pression commerciale, impatience | Discipline absolue, pas de dérogation |
| DKIM IONOS sélecteur dynamique manquant | Convention IONOS 3 sélecteurs non comprise (s1-ionos, s2-ionos, s42582890) | Vérifier les 3 sur sous-domaine, pousser le manquant via API |
| DMARC parent avec rua placeholder ou bidon | Doc copiée-collée jamais corrigée | Auditer le DMARC parent, mettre une vraie adresse |
| Sauter le test mail-tester | Croire que mes records DNS suffisent | Toujours >8/10 avant warmup |
| Ne pas vérifier les rapports DMARC | Détection tardive d'usurpation | Check hebdo dmarc@... |
| Display Name "noreply" ou "Newsletter" | Pattern marketing désuet | Préférer "L'équipe X" ou "Prénom de X" |
| Envoyer depuis l'apex du domaine | Mélange transactionnel + marketing | **Toujours sous-domaine dédié** (mail./pros./news.) |
| Backscatterer alarme mail-tester | IP partagée IONOS | Ignorer, n'affecte pas Gmail/Yahoo (passer Brevo SMTP plus tard) |

## BDD & scraping

| Risque | Mitigation |
|---|---|
| Acheter une BDD non opt-in pour SMS | RGPD + Bloctel + Orange/Bouygues blocking → ne **jamais** |
| BDD scrapée non validée → bounce massif | Email List Validation API systématique avant import Brevo |
| Doublons inter-sociétés | Dédoublonnage croisé global du groupe |
| Ne pas sauver la BDD | Sauvegarde mensuelle automatique (Google Drive ou S3) |
| BDD trop large mal segmentée | Segmenter par vertical, fraîcheur, engagement avant envoi |

## Pixels & tracking

| Risque | Cause racine | Mitigation |
|---|---|---|
| Branche mergée mais site non déployé | Merge ≠ déploiement auto | Toujours vérifier le déploiement après merge (Vercel/build)
| CAPI source = "Messages" au lieu de "Web" | Wizard Meta mal lu | Vérifier source "Web" pour tous les événements site
| CookieYes/complianz bloque le pixel | Consentement requis avant tracking | Vérifier que PixelYourSite est dans catégorie "marketing" ou configuré en mode essentiel
| CAPI token expiré | Token généré il y a +90j | Régénérer dans Events Manager > Paramètres > API Conversions
| Confondre site WordPress et landing Next.js | Même marque, stacks différentes | Documenter clairement : domaine = CMS = stack de tracking
| Pixels non mergés sur main | Branche fix jamais mergée | Vérifier git status + merge avant de dire "c'est fait"
| Wizard Meta "Associer" (1 clic sans code) | Tentation de cliquer | Ignorer sur site custom — ne marche que pour Shopify/partenaires
| Aucun événement ne remonte malgré config OK | Trafic quasi nul ou ad blocker | Meta Pixel Helper + vérifier trafic (CookieYes analytics)

## Pub & ads

| Risque | Mitigation |
|---|---|
| Lancer pub froide sans pixel mûr | Budget cramé, audiences vides → attendre J+28+ |
| Mélanger pixels de plusieurs marques | Attribution illisible → 1 BM par marque obligatoire |
| Frequency cap absent | Saturation audience, augmentation CPC | Cap 2-3 impressions/personne/semaine en froid |
| Créatives non renouvelées | Fatigue audience, CTR chute | Renouvellement toutes les 2 semaines |
| Lookalike sans seed audience suffisante | LAL inefficace | Min 100-300 convertis pour seed |
| iOS 14+ non géré | Perte tracking 30-50% | CAPI Meta + Google Enhanced Conversions obligatoires |

## Social & bots

| Risque | Mitigation |
|---|---|
| Bot LinkedIn à 200/jour dès le départ | Ban quasi-garanti | 20-30 max les 14 premiers jours, puis +20%/sem |
| Compte unique pour tous les bots | Ban = perte totale | Multi-comptes (3-5 par plateforme) |
| Messages bot identiques (pattern détectable) | Détection LinkedIn/Insta | Variations rotation messages |
| IP unique pour tous les bots | Détection ban en cascade | Multi-IP, multi-proxies |
| Comptes sociaux neufs lancés en pub direct | Algo Meta dégradé sur compte non-warmé | 14j+ d'activité organique avant 1ère pub |

## SEO

| Risque | Mitigation |
|---|---|
| Articles en rafale puis silence | Signal Google négatif (irrégularité) | Cadence régulière (1-3/sem stable) |
| Mots-clés trop concurrentiels en démarrage | Pas d'autorité domaine | Cibler longue traîne d'abord, autorité après |
| Backlinks toxiques (annuaires bas de gamme) | Pénalité Google | Disavow + qualité > quantité |
| Pas de schema.org | Manque référencement IA | Schema Organization + FAQPage + Article systématique |
| Site lent / non mobile | Core Web Vitals dégradés | Audit PageSpeed Insights régulier |

## SMS / WhatsApp / Postal

| Risque | Mitigation |
|---|---|
| SMS sans opt-in | Sanction CNIL + blocking opérateurs | Opt-in confirmé obligatoire |
| WhatsApp sans templates Meta validés | Blocage envoi | HSM templates validés en amont |
| Horaires indélicats | Plaintes massives | 10h-12h ou 14h-19h, jamais soir/week-end B2B |
| Postal sur BDD non qualifiée | ROI catastrophique (coût 0,80-2€/envoi) | Top 5-10% BDD uniquement |

## Phoning

| Risque | Mitigation |
|---|---|
| Cold call B2C sans Bloctel | Sanction CNIL | Vérifier Bloctel obligatoire pour B2C FR |
| Pas de scoring leads | Effort gaspillé | Appeler uniquement leads ayant engagé (open + clic) |
| Script générique | Faible taux de conversion | Scripts par persona, A/B testés |

## Multi-sociétés

| Risque | Mitigation |
|---|---|
| Lancer 5 sociétés en parallèle | Saturation production contenu | **Max 2-3 en parallèle**, jamais plus |
| Mutualiser BM Meta | Catastrophe attribution | 1 BM par société |
| Mutualiser compte Brevo | Mélange reputation | 1 compte par société recommandé |
| Pas de tracker des phases | Confusion sur où en est chaque société | Mettre à jour `etat-societes.md` à chaque action |
