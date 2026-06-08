# Rapport DMARC — 30 derniers jours

> Période : 2026-04-27 → 2026-05-27 (UTC)
> Généré le : 2026-05-27 08:00 UTC

## 📊 cuspide.fr

- **Rapports reçus** : 43
- **Volume emails** : 1181
- **Conformité DMARC** : 36.9% (436/1181)
  - ✅ DKIM + SPF tous deux OK : 407 (34.5%)
  - ✅ DKIM seul OK (forwarding) : 17 (1.4%)
  - ✅ SPF seul OK : 12 (1.0%)
  - 🚨 DKIM + SPF tous deux FAIL : 745 (63.1%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `209.85.220.41` | 751 | Google / Gmail forwarder | ⚠️ 1.9% |
| `212.227.126.187` | 28 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 24 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 23 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 22 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 21 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 20 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 20 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 20 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 18 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 16 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 15 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 15 | IONOS Mail SMTP | ✅ 100.0% |
| `54.240.6.245` | 14 | Amazon SES (Resend / app) | ✅ 100.0% |
| `54.240.3.27` | 13 | Amazon SES (Resend / app) | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `209.85.220.41` | 737 | Google / Gmail forwarder | `gmail.com` | `—` |
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

- **Rapports reçus** : 16
- **Volume emails** : 60
- **Conformité DMARC** : 93.3% (56/60)
  - ✅ DKIM + SPF tous deux OK : 38 (63.3%)
  - ✅ DKIM seul OK (forwarding) : 18 (30.0%)
  - ✅ SPF seul OK : 0 (0.0%)
  - 🚨 DKIM + SPF tous deux FAIL : 4 (6.7%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `82.165.159.8` | 8 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.6` | 6 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.37` | 5 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 5 | IONOS Mail SMTP | ⚠️ 60.0% |
| `82.165.159.44` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.10` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.39` | 3 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.9` | 2 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 2 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 2 | IONOS Mail SMTP | ⚠️ 50.0% |
| `217.72.192.73` | 2 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.7` | 1 | IONOS Mail SMTP | ✅ 100.0% |
| `82.165.159.5` | 1 | IONOS Mail SMTP | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `212.227.126.135` | 2 | IONOS Mail SMTP | `jak-company.com` | `partenariat.wei-wei.fr` |
| `212.227.17.13` | 1 | IONOS Mail SMTP | `jak-company.com` | `partenariat.wei-wei.fr` |
| `217.72.192.74` | 1 | IONOS Mail SMTP | `jak-company.com` | `partenariat.wei-wei.fr` |

> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation.

---

## 📊 news.cuspide.fr

- **Rapports reçus** : 41
- **Volume emails** : 504
- **Conformité DMARC** : 97.4% (491/504)
  - ✅ DKIM + SPF tous deux OK : 444 (88.1%)
  - ✅ DKIM seul OK (forwarding) : 46 (9.1%)
  - ✅ SPF seul OK : 1 (0.2%)
  - 🚨 DKIM + SPF tous deux FAIL : 13 (2.6%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `212.227.126.133` | 51 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.187` | 43 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 43 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 41 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 39 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 36 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 35 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 34 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 33 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 32 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 31 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 28 | IONOS Mail SMTP | ✅ 100.0% |
| `209.85.220.41` | 14 | Google / Gmail forwarder | ✅ 100.0% |
| `35.174.145.124` | 11 | Inconnu | 🚨 0.0% |
| `209.85.220.69` | 10 | Google / Gmail forwarder | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `35.174.145.124` | 11 | Inconnu | `news.cuspide.fr` | `news.cuspide.fr` |
| `2a01:111:f403:c107::3` | 1 | Inconnu | `cambayhealthcare.com` | `cambayhealthcare.onmicrosoft.com` |
| `2a01:111:f403:c107::9` | 1 | Inconnu | `cambayhealthcare.com` | `cambayhealthcare.onmicrosoft.com` |

> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation.

---

## 📊 pros.kelaj-company.com

- **Rapports reçus** : 40
- **Volume emails** : 392
- **Conformité DMARC** : 100.0% (392/392)
  - ✅ DKIM + SPF tous deux OK : 351 (89.5%)
  - ✅ DKIM seul OK (forwarding) : 41 (10.5%)
  - ✅ SPF seul OK : 0 (0.0%)
  - 🚨 DKIM + SPF tous deux FAIL : 0 (0.0%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `212.227.126.135` | 36 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 35 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 33 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 32 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 31 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 29 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 28 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 27 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 27 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 27 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.187` | 23 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 23 | IONOS Mail SMTP | ✅ 100.0% |
| `20.4.48.55` | 10 | Inconnu | ✅ 100.0% |
| `209.85.220.69` | 6 | Google / Gmail forwarder | ✅ 100.0% |
| `20.4.48.49` | 5 | Inconnu | ✅ 100.0% |

---
