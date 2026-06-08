# Rapport DMARC — 30 derniers jours

> Période : 2026-04-29 → 2026-05-29 (UTC)
> Généré le : 2026-05-29 08:00 UTC

## 📊 cuspide.fr

- **Rapports reçus** : 48
- **Volume emails** : 1310
- **Conformité DMARC** : 36.9% (483/1310)
  - ✅ DKIM + SPF tous deux OK : 448 (34.2%)
  - ✅ DKIM seul OK (forwarding) : 21 (1.6%)
  - ✅ SPF seul OK : 14 (1.1%)
  - 🚨 DKIM + SPF tous deux FAIL : 827 (63.1%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `209.85.220.41` | 837 | Google / Gmail forwarder | ⚠️ 2.2% |
| `212.227.126.187` | 29 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 26 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 25 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 23 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 22 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 21 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 21 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 21 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 19 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 18 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 18 | IONOS Mail SMTP | ✅ 100.0% |
| `54.240.6.245` | 17 | Amazon SES (Resend / app) | ✅ 100.0% |
| `54.240.6.27` | 16 | Amazon SES (Resend / app) | ✅ 100.0% |
| `217.72.192.73` | 16 | IONOS Mail SMTP | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `209.85.220.41` | 819 | Google / Gmail forwarder | `gmail.com` | `—` |
| `46.105.61.23` | 2 | OVH dedicated server | `fdgl.fr` | `cuspide.fr` |
| `209.85.128.44` | 1 | Google / Gmail forwarder | `gmail.com` | `—` |
| `209.85.128.52` | 1 | Google / Gmail forwarder | `gmail.com` | `—` |
| `209.85.128.53` | 1 | Google / Gmail forwarder | `gmail.com` | `—` |
| `209.85.221.49` | 1 | Google / Gmail forwarder | `gmail.com` | `—` |
| `46.105.77.232` | 1 | OVH dedicated server | `fdgl.fr` | `cuspide.fr` |
| `87.98.181.235` | 1 | Inconnu | `fdgl.fr` | `cuspide.fr` |

> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation.

---

## 📊 kelaj-company.com

- **Rapports reçus** : 19
- **Volume emails** : 67
- **Conformité DMARC** : 94.0% (63/67)
  - ✅ DKIM + SPF tous deux OK : 42 (62.7%)
  - ✅ DKIM seul OK (forwarding) : 21 (31.3%)
  - ✅ SPF seul OK : 0 (0.0%)
  - 🚨 DKIM + SPF tous deux FAIL : 4 (6.0%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `82.165.159.8` | 8 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.6` | 6 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.37` | 5 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 5 | IONOS Mail SMTP | ⚠️ 60.0% |
| `212.227.126.133` | 5 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.9` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.44` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.10` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.39` | 3 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 3 | IONOS Mail SMTP | ⚠️ 66.7% |
| `82.165.159.7` | 2 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 2 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 2 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 2 | IONOS Mail SMTP | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `212.227.126.135` | 2 | IONOS Mail SMTP | `jak-company.com` | `partenariat.wei-wei.fr` |
| `212.227.17.13` | 1 | IONOS Mail SMTP | `jak-company.com` | `partenariat.wei-wei.fr` |
| `217.72.192.74` | 1 | IONOS Mail SMTP | `jak-company.com` | `partenariat.wei-wei.fr` |

> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation.

---

## 📊 news.cuspide.fr

- **Rapports reçus** : 45
- **Volume emails** : 559
- **Conformité DMARC** : 97.0% (542/559)
  - ✅ DKIM + SPF tous deux OK : 490 (87.7%)
  - ✅ DKIM seul OK (forwarding) : 51 (9.1%)
  - ✅ SPF seul OK : 1 (0.2%)
  - 🚨 DKIM + SPF tous deux FAIL : 17 (3.0%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `212.227.126.133` | 53 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.187` | 51 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 47 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 45 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 41 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 41 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 38 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 38 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 38 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 36 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 34 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 30 | IONOS Mail SMTP | ✅ 100.0% |
| `209.85.220.41` | 17 | Google / Gmail forwarder | ✅ 100.0% |
| `35.174.145.124` | 15 | Inconnu | 🚨 0.0% |
| `209.85.220.69` | 11 | Google / Gmail forwarder | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `35.174.145.124` | 15 | Inconnu | `news.cuspide.fr` | `news.cuspide.fr` |
| `2a01:111:f403:c107::3` | 1 | Inconnu | `cambayhealthcare.com` | `cambayhealthcare.onmicrosoft.com` |
| `2a01:111:f403:c107::9` | 1 | Inconnu | `cambayhealthcare.com` | `cambayhealthcare.onmicrosoft.com` |

> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation.

---

## 📊 pros.kelaj-company.com

- **Rapports reçus** : 45
- **Volume emails** : 482
- **Conformité DMARC** : 99.2% (478/482)
  - ✅ DKIM + SPF tous deux OK : 429 (89.0%)
  - ✅ DKIM seul OK (forwarding) : 49 (10.2%)
  - ✅ SPF seul OK : 0 (0.0%)
  - 🚨 DKIM + SPF tous deux FAIL : 4 (0.8%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `212.227.126.135` | 43 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 42 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 41 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 38 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 36 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 35 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 35 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 34 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 34 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 33 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 31 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.187` | 27 | IONOS Mail SMTP | ✅ 100.0% |
| `209.85.220.69` | 13 | Google / Gmail forwarder | ⚠️ 69.2% |
| `20.4.48.55` | 10 | Inconnu | ✅ 100.0% |
| `209.85.220.41` | 7 | Google / Gmail forwarder | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `209.85.220.69` | 4 | Google / Gmail forwarder | `qa.tech` | `qa.tech` |

> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation.

---
