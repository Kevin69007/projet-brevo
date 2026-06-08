# Rapport DMARC — 30 derniers jours

> Période : 2026-04-30 → 2026-05-30 (UTC)
> Généré le : 2026-05-30 08:10 UTC

## 📊 cuspide.fr

- **Rapports reçus** : 51
- **Volume emails** : 1344
- **Conformité DMARC** : 38.0% (511/1344)
  - ✅ DKIM + SPF tous deux OK : 474 (35.3%)
  - ✅ DKIM seul OK (forwarding) : 21 (1.6%)
  - ✅ SPF seul OK : 16 (1.2%)
  - 🚨 DKIM + SPF tous deux FAIL : 833 (62.0%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `209.85.220.41` | 843 | Google / Gmail forwarder | ⚠️ 2.1% |
| `212.227.126.187` | 30 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 27 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 26 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 25 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 24 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 24 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 22 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 21 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 20 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 20 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 18 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 18 | IONOS Mail SMTP | ✅ 100.0% |
| `54.240.6.245` | 17 | Amazon SES (Resend / app) | ✅ 100.0% |
| `54.240.6.27` | 16 | Amazon SES (Resend / app) | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `209.85.220.41` | 825 | Google / Gmail forwarder | `gmail.com` | `—` |
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

- **Rapports reçus** : 20
- **Volume emails** : 69
- **Conformité DMARC** : 94.2% (65/69)
  - ✅ DKIM + SPF tous deux OK : 42 (60.9%)
  - ✅ DKIM seul OK (forwarding) : 23 (33.3%)
  - ✅ SPF seul OK : 0 (0.0%)
  - 🚨 DKIM + SPF tous deux FAIL : 4 (5.8%)

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
| `217.72.192.74` | 4 | IONOS Mail SMTP | ⚠️ 75.0% |
| `212.227.126.131` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.39` | 3 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.7` | 2 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 2 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 2 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 2 | IONOS Mail SMTP | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `212.227.126.135` | 2 | IONOS Mail SMTP | `jak-company.com` | `partenariat.wei-wei.fr` |
| `212.227.17.13` | 1 | IONOS Mail SMTP | `jak-company.com` | `partenariat.wei-wei.fr` |
| `217.72.192.74` | 1 | IONOS Mail SMTP | `jak-company.com` | `partenariat.wei-wei.fr` |

> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation.

---

## 📊 news.cuspide.fr

- **Rapports reçus** : 47
- **Volume emails** : 583
- **Conformité DMARC** : 97.1% (566/583)
  - ✅ DKIM + SPF tous deux OK : 514 (88.2%)
  - ✅ DKIM seul OK (forwarding) : 51 (8.7%)
  - ✅ SPF seul OK : 1 (0.2%)
  - 🚨 DKIM + SPF tous deux FAIL : 17 (2.9%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `212.227.126.133` | 56 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.187` | 54 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 49 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 46 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 45 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 42 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 41 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 40 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 40 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 37 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 35 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 31 | IONOS Mail SMTP | ✅ 100.0% |
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

- **Rapports reçus** : 48
- **Volume emails** : 564
- **Conformité DMARC** : 98.8% (557/564)
  - ✅ DKIM + SPF tous deux OK : 502 (89.0%)
  - ✅ DKIM seul OK (forwarding) : 55 (9.8%)
  - ✅ SPF seul OK : 0 (0.0%)
  - 🚨 DKIM + SPF tous deux FAIL : 7 (1.2%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `212.227.126.135` | 51 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 50 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 49 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 47 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 44 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 41 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 40 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 40 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 37 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 35 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 35 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.187` | 33 | IONOS Mail SMTP | ✅ 100.0% |
| `209.85.220.69` | 19 | Google / Gmail forwarder | ⚠️ 63.2% |
| `20.4.48.55` | 10 | Inconnu | ✅ 100.0% |
| `209.85.220.41` | 9 | Google / Gmail forwarder | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `209.85.220.69` | 4 | Google / Gmail forwarder | `qa.tech` | `qa.tech` |
| `209.85.220.69` | 3 | Google / Gmail forwarder | `onyxproject.com` | `onyxproject-com.20251104.gappssmtp.com` |

> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation.

---
