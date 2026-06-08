# Rapport DMARC — 30 derniers jours

> Période : 2026-05-04 → 2026-06-03 (UTC)
> Généré le : 2026-06-03 08:00 UTC

## 📊 cuspide.fr

- **Rapports reçus** : 64
- **Volume emails** : 1648
- **Conformité DMARC** : 39.3% (648/1648)
  - ✅ DKIM + SPF tous deux OK : 600 (36.4%)
  - ✅ DKIM seul OK (forwarding) : 28 (1.7%)
  - ✅ SPF seul OK : 20 (1.2%)
  - 🚨 DKIM + SPF tous deux FAIL : 1000 (60.7%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `209.85.220.41` | 1012 | Google / Gmail forwarder | ⚠️ 2.0% |
| `217.72.192.75` | 38 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.187` | 38 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 38 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 35 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 34 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 33 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 32 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 30 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 29 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 28 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 25 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 24 | IONOS Mail SMTP | ✅ 100.0% |
| `54.240.6.27` | 20 | Amazon SES (Resend / app) | ✅ 100.0% |
| `54.240.6.245` | 18 | Amazon SES (Resend / app) | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `209.85.220.41` | 992 | Google / Gmail forwarder | `gmail.com` | `—` |
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

- **Rapports reçus** : 23
- **Volume emails** : 73
- **Conformité DMARC** : 94.5% (69/73)
  - ✅ DKIM + SPF tous deux OK : 42 (57.5%)
  - ✅ DKIM seul OK (forwarding) : 27 (37.0%)
  - ✅ SPF seul OK : 0 (0.0%)
  - 🚨 DKIM + SPF tous deux FAIL : 4 (5.5%)

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

- **Rapports reçus** : 55
- **Volume emails** : 689
- **Conformité DMARC** : 97.4% (671/689)
  - ✅ DKIM + SPF tous deux OK : 605 (87.8%)
  - ✅ DKIM seul OK (forwarding) : 65 (9.4%)
  - ✅ SPF seul OK : 1 (0.1%)
  - 🚨 DKIM + SPF tous deux FAIL : 18 (2.6%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `212.227.126.187` | 62 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 61 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 59 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 57 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 56 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 48 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 48 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 47 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 44 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 44 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 43 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 38 | IONOS Mail SMTP | ✅ 100.0% |
| `209.85.220.41` | 19 | Google / Gmail forwarder | ✅ 100.0% |
| `35.174.145.124` | 16 | Inconnu | 🚨 0.0% |
| `209.85.220.69` | 16 | Google / Gmail forwarder | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `35.174.145.124` | 16 | Inconnu | `news.cuspide.fr` | `news.cuspide.fr` |
| `2a01:111:f403:c107::3` | 1 | Inconnu | `cambayhealthcare.com` | `cambayhealthcare.onmicrosoft.com` |
| `2a01:111:f403:c107::9` | 1 | Inconnu | `cambayhealthcare.com` | `cambayhealthcare.onmicrosoft.com` |

> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation.

---

## 📊 pros.kelaj-company.com

- **Rapports reçus** : 59
- **Volume emails** : 799
- **Conformité DMARC** : 98.6% (788/799)
  - ✅ DKIM + SPF tous deux OK : 701 (87.7%)
  - ✅ DKIM seul OK (forwarding) : 87 (10.9%)
  - ✅ SPF seul OK : 0 (0.0%)
  - 🚨 DKIM + SPF tous deux FAIL : 11 (1.4%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `212.227.126.135` | 79 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 66 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 64 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 60 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 59 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 59 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 58 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 57 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 52 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 52 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 50 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.187` | 46 | IONOS Mail SMTP | ✅ 100.0% |
| `209.85.220.69` | 27 | Google / Gmail forwarder | ⚠️ 59.3% |
| `209.85.220.41` | 18 | Google / Gmail forwarder | ✅ 100.0% |
| `20.4.48.55` | 12 | Inconnu | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `209.85.220.69` | 8 | Google / Gmail forwarder | `qa.tech` | `qa.tech` |
| `209.85.220.69` | 3 | Google / Gmail forwarder | `onyxproject.com` | `onyxproject-com.20251104.gappssmtp.com` |

> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation.

---
