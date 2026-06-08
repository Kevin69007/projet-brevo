# Rapport DMARC — 30 derniers jours

> Période : 2026-05-03 → 2026-06-02 (UTC)
> Généré le : 2026-06-02 08:00 UTC

## 📊 cuspide.fr

- **Rapports reçus** : 61
- **Volume emails** : 1486
- **Conformité DMARC** : 39.2% (583/1486)
  - ✅ DKIM + SPF tous deux OK : 542 (36.5%)
  - ✅ DKIM seul OK (forwarding) : 22 (1.5%)
  - ✅ SPF seul OK : 19 (1.3%)
  - 🚨 DKIM + SPF tous deux FAIL : 903 (60.8%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `209.85.220.41` | 913 | Google / Gmail forwarder | ⚠️ 2.0% |
| `212.227.126.187` | 35 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 33 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 31 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 30 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 28 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 28 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 26 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 26 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 23 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 22 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 22 | IONOS Mail SMTP | ✅ 100.0% |
| `54.240.6.27` | 20 | Amazon SES (Resend / app) | ✅ 100.0% |
| `212.227.126.131` | 20 | IONOS Mail SMTP | ✅ 100.0% |
| `54.240.6.245` | 18 | Amazon SES (Resend / app) | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `209.85.220.41` | 895 | Google / Gmail forwarder | `gmail.com` | `—` |
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

- **Rapports reçus** : 22
- **Volume emails** : 72
- **Conformité DMARC** : 94.4% (68/72)
  - ✅ DKIM + SPF tous deux OK : 42 (58.3%)
  - ✅ DKIM seul OK (forwarding) : 26 (36.1%)
  - ✅ SPF seul OK : 0 (0.0%)
  - 🚨 DKIM + SPF tous deux FAIL : 4 (5.6%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `82.165.159.8` | 8 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.6` | 6 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 6 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.37` | 5 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 5 | IONOS Mail SMTP | ⚠️ 60.0% |
| `82.165.159.9` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.44` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.10` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 4 | IONOS Mail SMTP | ⚠️ 75.0% |
| `212.227.126.131` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.39` | 3 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 3 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 3 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.7` | 2 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 2 | IONOS Mail SMTP | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `212.227.126.135` | 2 | IONOS Mail SMTP | `jak-company.com` | `partenariat.wei-wei.fr` |
| `212.227.17.13` | 1 | IONOS Mail SMTP | `jak-company.com` | `partenariat.wei-wei.fr` |
| `217.72.192.74` | 1 | IONOS Mail SMTP | `jak-company.com` | `partenariat.wei-wei.fr` |

> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation.

---

## 📊 news.cuspide.fr

- **Rapports reçus** : 53
- **Volume emails** : 664
- **Conformité DMARC** : 97.3% (646/664)
  - ✅ DKIM + SPF tous deux OK : 583 (87.8%)
  - ✅ DKIM seul OK (forwarding) : 62 (9.3%)
  - ✅ SPF seul OK : 1 (0.2%)
  - 🚨 DKIM + SPF tous deux FAIL : 18 (2.7%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `212.227.126.187` | 61 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 60 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 57 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 55 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 54 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 46 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 46 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 44 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 42 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 42 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 41 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 37 | IONOS Mail SMTP | ✅ 100.0% |
| `209.85.220.41` | 19 | Google / Gmail forwarder | ✅ 100.0% |
| `35.174.145.124` | 16 | Inconnu | 🚨 0.0% |
| `209.85.220.69` | 14 | Google / Gmail forwarder | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `35.174.145.124` | 16 | Inconnu | `news.cuspide.fr` | `news.cuspide.fr` |
| `2a01:111:f403:c107::3` | 1 | Inconnu | `cambayhealthcare.com` | `cambayhealthcare.onmicrosoft.com` |
| `2a01:111:f403:c107::9` | 1 | Inconnu | `cambayhealthcare.com` | `cambayhealthcare.onmicrosoft.com` |

> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation.

---

## 📊 pros.kelaj-company.com

- **Rapports reçus** : 56
- **Volume emails** : 733
- **Conformité DMARC** : 98.5% (722/733)
  - ✅ DKIM + SPF tous deux OK : 643 (87.7%)
  - ✅ DKIM seul OK (forwarding) : 79 (10.8%)
  - ✅ SPF seul OK : 0 (0.0%)
  - 🚨 DKIM + SPF tous deux FAIL : 11 (1.5%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `212.227.126.135` | 66 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 61 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 61 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 57 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 56 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 54 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 54 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 53 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 48 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 45 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 45 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.187` | 43 | IONOS Mail SMTP | ✅ 100.0% |
| `209.85.220.69` | 25 | Google / Gmail forwarder | ⚠️ 56.0% |
| `209.85.220.41` | 15 | Google / Gmail forwarder | ✅ 100.0% |
| `20.4.48.55` | 12 | Inconnu | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `209.85.220.69` | 8 | Google / Gmail forwarder | `qa.tech` | `qa.tech` |
| `209.85.220.69` | 3 | Google / Gmail forwarder | `onyxproject.com` | `onyxproject-com.20251104.gappssmtp.com` |

> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation.

---
