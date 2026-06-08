# Rapport DMARC — 7 derniers jours

> Période : 2026-05-26 → 2026-06-02 (UTC)
> Généré le : 2026-06-02 08:00 UTC

## 📊 cuspide.fr

- **Rapports reçus** : 14
- **Volume emails** : 228
- **Conformité DMARC** : 54.8% (125/228)
  - ✅ DKIM + SPF tous deux OK : 117 (51.3%)
  - ✅ DKIM seul OK (forwarding) : 3 (1.3%)
  - ✅ SPF seul OK : 5 (2.2%)
  - 🚨 DKIM + SPF tous deux FAIL : 103 (45.2%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `209.85.220.41` | 105 | Google / Gmail forwarder | ⚠️ 1.9% |
| `217.72.192.75` | 12 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 8 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.187` | 7 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 7 | IONOS Mail SMTP | ✅ 100.0% |
| `54.240.6.53` | 6 | Amazon SES (Resend / app) | ✅ 100.0% |
| `54.240.6.27` | 6 | Amazon SES (Resend / app) | ✅ 100.0% |
| `217.72.192.73` | 6 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 6 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 6 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 6 | IONOS Mail SMTP | ✅ 100.0% |
| `54.240.3.25` | 5 | Amazon SES (Resend / app) | ✅ 100.0% |
| `217.72.192.74` | 5 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 5 | IONOS Mail SMTP | ✅ 100.0% |
| `54.240.6.244` | 4 | Amazon SES (Resend / app) | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `209.85.220.41` | 103 | Google / Gmail forwarder | `gmail.com` | `—` |

> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation.

---

## 📊 kelaj-company.com

- **Rapports reçus** : 3
- **Volume emails** : 5
- **Conformité DMARC** : 100.0% (5/5)
  - ✅ DKIM + SPF tous deux OK : 0 (0.0%)
  - ✅ DKIM seul OK (forwarding) : 5 (100.0%)
  - ✅ SPF seul OK : 0 (0.0%)
  - 🚨 DKIM + SPF tous deux FAIL : 0 (0.0%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `217.72.192.74` | 1 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 1 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 1 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 1 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 1 | IONOS Mail SMTP | ✅ 100.0% |

---

## 📊 news.cuspide.fr

- **Rapports reçus** : 9
- **Volume emails** : 120
- **Conformité DMARC** : 99.2% (119/120)
  - ✅ DKIM + SPF tous deux OK : 105 (87.5%)
  - ✅ DKIM seul OK (forwarding) : 14 (11.7%)
  - ✅ SPF seul OK : 0 (0.0%)
  - 🚨 DKIM + SPF tous deux FAIL : 1 (0.8%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `217.72.192.74` | 14 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 12 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 11 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.187` | 11 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 11 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 10 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 9 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 7 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 7 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 7 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `209.85.220.69` | 4 | Google / Gmail forwarder | ✅ 100.0% |
| `209.85.220.41` | 4 | Google / Gmail forwarder | ✅ 100.0% |
| `212.227.17.13` | 2 | IONOS Mail SMTP | ✅ 100.0% |
| `35.174.145.124` | 1 | Inconnu | 🚨 0.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `35.174.145.124` | 1 | Inconnu | `news.cuspide.fr` | `news.cuspide.fr` |

> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation.

---

## 📊 pros.kelaj-company.com

- **Rapports reçus** : 12
- **Volume emails** : 296
- **Conformité DMARC** : 96.3% (285/296)
  - ✅ DKIM + SPF tous deux OK : 249 (84.1%)
  - ✅ DKIM seul OK (forwarding) : 36 (12.2%)
  - ✅ SPF seul OK : 0 (0.0%)
  - 🚨 DKIM + SPF tous deux FAIL : 11 (3.7%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `212.227.126.135` | 26 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 26 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 25 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 24 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 22 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 22 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 20 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 20 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.187` | 19 | IONOS Mail SMTP | ✅ 100.0% |
| `209.85.220.69` | 18 | Google / Gmail forwarder | ⚠️ 38.9% |
| `212.227.17.24` | 15 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 15 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 15 | IONOS Mail SMTP | ✅ 100.0% |
| `209.85.220.41` | 10 | Google / Gmail forwarder | ✅ 100.0% |
| `2600:1901:101:11::2` | 2 | Inconnu | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `209.85.220.69` | 8 | Google / Gmail forwarder | `qa.tech` | `qa.tech` |
| `209.85.220.69` | 3 | Google / Gmail forwarder | `onyxproject.com` | `onyxproject-com.20251104.gappssmtp.com` |

> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation.

---
