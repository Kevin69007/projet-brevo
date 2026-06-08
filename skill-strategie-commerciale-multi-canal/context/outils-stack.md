# Outils & stack — Hub Brevo

Référence des outils utilisés par le hub multi-sociétés Cuspide/JAK.

## Email & délivrabilité

| Outil | Rôle | Lien |
|---|---|---|
| Brevo (ex-Sendinblue) | Envoi emails marketing & transactionnels, automation | https://app.brevo.com |
| IONOS Mail | Hébergement mailboxes (Mail Basic / Business) | https://mail.ionos.fr |
| Allegrow / Neverspam | Warmup mailbox + monitoring reputation | https://app.neverspam.io |
| Email List Validation | Validation deliverability des adresses (avant envoi) | API via skill |
| Mail-tester | Test score authentification & contenu (10/10 visé) | https://www.mail-tester.com |
| MXToolbox | Vérif DNS, blacklists, SPF/DKIM/DMARC | https://mxtoolbox.com |
| dmarcian | Parsing rapports DMARC XML | https://dmarcian.com |

## Tracking & attribution

| Outil | Rôle |
|---|---|
| Switchy | Shortlinks trackés, A/B test liens, retargeting pixel sur clic |
| Metricool | Planification publications + analytics social |
| Looker Studio | Dashboards centralisés (Brevo, Meta Ads, Google Ads, GA4, Search Console) |
| Google Analytics 4 (GA4) | Web analytics |
| Google Search Console | SEO performances |

## Scraping & enrichissement

| Outil | Rôle |
|---|---|
| Octoparse | Scraping no-code sites web complexes |
| Apify | Scraping LinkedIn Sales Navigator, Google Maps, etc. |
| TexAu | Automation LinkedIn (visites, invitations, messages) |
| Dropcontact | Enrichissement data B2B (emails pros à partir nom+entreprise) |
| Hunter | Recherche emails par domaine |
| FindThatLead | Enrichissement multi-sources |

## Quiz / Lead magnets

| Outil | Rôle |
|---|---|
| Marquiz | Quiz interactifs lead magnets |
| Woorise | Concours, quiz, formulaires lead-gen |

## Bot & outreach

| Outil | Rôle |
|---|---|
| ZeroWork | Automation tâches récurrentes (LinkedIn, Insta, etc.) |
| TexAu | LinkedIn outreach automation |
| Encharge | Marketing automation cross-channel |

## Pub & ads

| Plateforme | Catégorie |
|---|---|
| Meta Ads Manager | Facebook + Instagram (CAPI obligatoire) |
| Google Ads | Search + Display + YouTube + Shopping |
| TikTok Ads | Vidéo court B2C |
| LinkedIn Ads | B2B (cher mais ciblage précis) |
| Snapchat Ads | B2C jeune |

## Pixels & tracking (site)

| Outil | Stack | Rôle |
|---|---|---|
| PixelYourSite | WordPress/WooCommerce | Meta Pixel + CAPI + Advanced Matching (setup en 5 min) |
| Code custom | Next.js/React | Injection manuelle fbevents.js + helpers tracking |
| Meta Pixel Helper | Extension Chrome | Vérification live des événements |
| Google Tag Manager | Tous | Centralisation tags (GA4, LinkedIn, Meta, etc.) |

## CRM & lead management

| Outil | Rôle |
|---|---|
| Brevo CRM | CRM intégré aux campagnes |
| Encharge | Automation cross-channel + nurturing |

## SMS / WhatsApp / Postal

| Outil | Rôle |
|---|---|
| Brevo SMS | SMS marketing volumes faibles-moyens |
| Sarbacane / Esendex | SMS marketing volumes élevés |
| Brevo WhatsApp | WhatsApp Business via Brevo |
| Twilio / WATI | WhatsApp Business avancé |
| Mediapost / La Poste Pro | Mailing postal |

## Visuel & contenu

| Outil | Rôle |
|---|---|
| Nexweave | Personnalisation vidéo (vidéos avec prénom du destinataire) |
| Canva | Création visuels rapides |
| Adobe Creative Suite | Production pro |

## Clés API utilisées (dans `brevo-secrets.env`)

- `BREVO_API_KEY` — envois Brevo
- `IONOS_API_PREFIX` + `IONOS_API_SECRET` — DNS API IONOS (zones du compte)
- `ALLEGROW_API_KEY` + `ALLEGROW_API_KEY_ID` — validation emails (pas stats)

## Comptes et accès

- Compte central Brevo : 11 352 contacts, 9 975 crédits (au 05/05/2026)
- Compte Allegrow : AppSumo Premium, 2500 crédits validation, slots warmup multiples
- Login Allegrow : passwordless via `contact@jak-company.com` (code 6 chiffres email)
- Zones IONOS gérées : cuspide.fr, kelaj-company.com, jak-company.com, besmilecare.fr, formations-dentaire.fr, kevin-attallah.com, monlabodepoche.{com,eu,fr,org}, padel-stars.fr, ridgedigitallab.com
