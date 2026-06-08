# Rapport DMARC — 30 derniers jours

> Période : 2026-05-05 → 2026-06-04 (UTC)
> Généré le : 2026-06-04 08:00 UTC

## 📊 cuspide.fr

- **Rapports reçus** : 66
- **Volume emails** : 1763
- **Conformité DMARC** : 38.2% (674/1763)
  - ✅ DKIM + SPF tous deux OK : 624 (35.4%)
  - ✅ DKIM seul OK (forwarding) : 30 (1.7%)
  - ✅ SPF seul OK : 20 (1.1%)
  - 🚨 DKIM + SPF tous deux FAIL : 1089 (61.8%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `209.85.220.41` | 1103 | Google / Gmail forwarder | ⚠️ 2.0% |
| `217.72.192.75` | 41 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 40 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.187` | 39 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 37 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 35 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 34 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 31 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 31 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 30 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 29 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 27 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 25 | IONOS Mail SMTP | ✅ 100.0% |
| `54.240.6.27` | 20 | Amazon SES (Resend / app) | ✅ 100.0% |
| `54.240.6.53` | 19 | Amazon SES (Resend / app) | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `209.85.220.41` | 1081 | Google / Gmail forwarder | `gmail.com` | `—` |
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

- **Rapports reçus** : 56
- **Volume emails** : 712
- **Conformité DMARC** : 97.5% (694/712)
  - ✅ DKIM + SPF tous deux OK : 627 (88.1%)
  - ✅ DKIM seul OK (forwarding) : 66 (9.3%)
  - ✅ SPF seul OK : 1 (0.1%)
  - 🚨 DKIM + SPF tous deux FAIL : 18 (2.5%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `212.227.126.187` | 63 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 60 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 60 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 59 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 56 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 53 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 49 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 49 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 48 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 47 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 46 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 39 | IONOS Mail SMTP | ✅ 100.0% |
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

- **Rapports reçus** : 61
- **Volume emails** : 886
- **Conformité DMARC** : 98.2% (870/886)
  - ✅ DKIM + SPF tous deux OK : 771 (87.0%)
  - ✅ DKIM seul OK (forwarding) : 98 (11.1%)
  - ✅ SPF seul OK : 1 (0.1%)
  - 🚨 DKIM + SPF tous deux FAIL : 16 (1.8%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `212.227.126.135` | 85 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 75 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 69 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 66 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 65 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 63 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 62 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 59 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 59 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 57 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.187` | 57 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 57 | IONOS Mail SMTP | ✅ 100.0% |
| `209.85.220.69` | 32 | Google / Gmail forwarder | ⚠️ 53.1% |
| `209.85.220.41` | 21 | Google / Gmail forwarder | ✅ 100.0% |
| `20.4.48.55` | 13 | Inconnu | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `209.85.220.69` | 12 | Google / Gmail forwarder | `qa.tech` | `qa.tech` |
| `209.85.220.69` | 3 | Google / Gmail forwarder | `onyxproject.com` | `onyxproject-com.20251104.gappssmtp.com` |
| `35.174.145.124` | 1 | Inconnu | `pros.kelaj-company.com` | `pros.kelaj-company.com` |

> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation.

---
