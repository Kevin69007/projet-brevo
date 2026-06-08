# Rapport DMARC — 30 derniers jours

> Période : 2026-04-28 → 2026-05-28 (UTC)
> Généré le : 2026-05-28 08:00 UTC

## 📊 cuspide.fr

- **Rapports reçus** : 45
- **Volume emails** : 1256
- **Conformité DMARC** : 36.3% (456/1256)
  - ✅ DKIM + SPF tous deux OK : 423 (33.7%)
  - ✅ DKIM seul OK (forwarding) : 19 (1.5%)
  - ✅ SPF seul OK : 14 (1.1%)
  - 🚨 DKIM + SPF tous deux FAIL : 800 (63.7%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `209.85.220.41` | 808 | Google / Gmail forwarder | ⚠️ 2.0% |
| `212.227.126.187` | 28 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 25 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 24 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 22 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 21 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 21 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 21 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 20 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 18 | IONOS Mail SMTP | ✅ 100.0% |
| `54.240.6.245` | 17 | Amazon SES (Resend / app) | ✅ 100.0% |
| `212.227.126.133` | 17 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 17 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 16 | IONOS Mail SMTP | ✅ 100.0% |
| `54.240.6.27` | 14 | Amazon SES (Resend / app) | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `209.85.220.41` | 792 | Google / Gmail forwarder | `gmail.com` | `—` |
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

- **Rapports reçus** : 18
- **Volume emails** : 65
- **Conformité DMARC** : 93.8% (61/65)
  - ✅ DKIM + SPF tous deux OK : 42 (64.6%)
  - ✅ DKIM seul OK (forwarding) : 19 (29.2%)
  - ✅ SPF seul OK : 0 (0.0%)
  - 🚨 DKIM + SPF tous deux FAIL : 4 (6.2%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `82.165.159.8` | 8 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.6` | 6 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.37` | 5 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 5 | IONOS Mail SMTP | ⚠️ 60.0% |
| `82.165.159.9` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.44` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.10` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.39` | 3 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.7` | 2 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 2 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 2 | IONOS Mail SMTP | ⚠️ 50.0% |
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

- **Rapports reçus** : 43
- **Volume emails** : 533
- **Conformité DMARC** : 97.2% (518/533)
  - ✅ DKIM + SPF tous deux OK : 470 (88.2%)
  - ✅ DKIM seul OK (forwarding) : 47 (8.8%)
  - ✅ SPF seul OK : 1 (0.2%)
  - 🚨 DKIM + SPF tous deux FAIL : 15 (2.8%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `212.227.126.133` | 52 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.187` | 49 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 45 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 44 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 39 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 38 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 37 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 36 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 35 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 35 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 32 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 30 | IONOS Mail SMTP | ✅ 100.0% |
| `209.85.220.41` | 15 | Google / Gmail forwarder | ✅ 100.0% |
| `35.174.145.124` | 13 | Inconnu | 🚨 0.0% |
| `209.85.220.69` | 10 | Google / Gmail forwarder | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `35.174.145.124` | 13 | Inconnu | `news.cuspide.fr` | `news.cuspide.fr` |
| `2a01:111:f403:c107::3` | 1 | Inconnu | `cambayhealthcare.com` | `cambayhealthcare.onmicrosoft.com` |
| `2a01:111:f403:c107::9` | 1 | Inconnu | `cambayhealthcare.com` | `cambayhealthcare.onmicrosoft.com` |

> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation.

---

## 📊 pros.kelaj-company.com

- **Rapports reçus** : 43
- **Volume emails** : 427
- **Conformité DMARC** : 100.0% (427/427)
  - ✅ DKIM + SPF tous deux OK : 384 (89.9%)
  - ✅ DKIM seul OK (forwarding) : 43 (10.1%)
  - ✅ SPF seul OK : 0 (0.0%)
  - 🚨 DKIM + SPF tous deux FAIL : 0 (0.0%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `212.227.126.135` | 39 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 37 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 35 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 34 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 34 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 31 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 31 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 30 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 30 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 30 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 29 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.187` | 24 | IONOS Mail SMTP | ✅ 100.0% |
| `20.4.48.55` | 10 | Inconnu | ✅ 100.0% |
| `209.85.220.69` | 7 | Google / Gmail forwarder | ✅ 100.0% |
| `209.85.220.41` | 5 | Google / Gmail forwarder | ✅ 100.0% |

---
