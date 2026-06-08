# Rapport DMARC — 7 derniers jours

> Période : 2026-05-27 → 2026-06-03 (UTC)
> Généré le : 2026-06-03 08:00 UTC

## 📊 cuspide.fr

- **Rapports reçus** : 14
- **Volume emails** : 336
- **Conformité DMARC** : 48.5% (163/336)
  - ✅ DKIM + SPF tous deux OK : 150 (44.6%)
  - ✅ DKIM seul OK (forwarding) : 7 (2.1%)
  - ✅ SPF seul OK : 6 (1.8%)
  - 🚨 DKIM + SPF tous deux FAIL : 173 (51.5%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `209.85.220.41` | 175 | Google / Gmail forwarder | ⚠️ 1.1% |
| `217.72.192.75` | 16 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 16 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 12 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 12 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 11 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 11 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 9 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 9 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.187` | 9 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 7 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 7 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 5 | IONOS Mail SMTP | ✅ 100.0% |
| `54.240.6.53` | 4 | Amazon SES (Resend / app) | ✅ 100.0% |
| `54.240.6.27` | 4 | Amazon SES (Resend / app) | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `209.85.220.41` | 173 | Google / Gmail forwarder | `gmail.com` | `—` |

> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation.

---

## 📊 kelaj-company.com

- **Rapports reçus** : 3
- **Volume emails** : 4
- **Conformité DMARC** : 100.0% (4/4)
  - ✅ DKIM + SPF tous deux OK : 0 (0.0%)
  - ✅ DKIM seul OK (forwarding) : 4 (100.0%)
  - ✅ SPF seul OK : 0 (0.0%)
  - 🚨 DKIM + SPF tous deux FAIL : 0 (0.0%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `217.72.192.73` | 1 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.187` | 1 | IONOS Mail SMTP | ✅ 100.0% |
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
| `217.72.192.75` | 14 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 14 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 12 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 10 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.187` | 10 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 9 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 8 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 8 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 6 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 6 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 6 | IONOS Mail SMTP | ✅ 100.0% |
| `209.85.220.69` | 5 | Google / Gmail forwarder | ✅ 100.0% |
| `212.227.17.13` | 2 | IONOS Mail SMTP | ✅ 100.0% |
| `209.85.220.41` | 2 | Google / Gmail forwarder | ✅ 100.0% |
| `35.174.145.124` | 1 | Inconnu | 🚨 0.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `35.174.145.124` | 1 | Inconnu | `news.cuspide.fr` | `news.cuspide.fr` |

> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation.

---

## 📊 pros.kelaj-company.com

- **Rapports reçus** : 13
- **Volume emails** : 295
- **Conformité DMARC** : 97.6% (288/295)
  - ✅ DKIM + SPF tous deux OK : 251 (85.1%)
  - ✅ DKIM seul OK (forwarding) : 37 (12.5%)
  - ✅ SPF seul OK : 0 (0.0%)
  - 🚨 DKIM + SPF tous deux FAIL : 7 (2.4%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `212.227.126.135` | 35 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 23 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 23 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 22 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 21 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 21 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 21 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 20 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.187` | 18 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 18 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 18 | IONOS Mail SMTP | ✅ 100.0% |
| `209.85.220.69` | 14 | Google / Gmail forwarder | ⚠️ 50.0% |
| `212.227.17.24` | 12 | IONOS Mail SMTP | ✅ 100.0% |
| `209.85.220.41` | 11 | Google / Gmail forwarder | ✅ 100.0% |
| `2600:1901:101:11::2` | 2 | Inconnu | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `209.85.220.69` | 4 | Google / Gmail forwarder | `qa.tech` | `qa.tech` |
| `209.85.220.69` | 3 | Google / Gmail forwarder | `onyxproject.com` | `onyxproject-com.20251104.gappssmtp.com` |

> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation.

---
