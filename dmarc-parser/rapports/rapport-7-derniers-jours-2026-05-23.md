# Rapport DMARC — 7 derniers jours

> Période : 2026-05-16 → 2026-05-23 (UTC)
> Généré le : 2026-05-23 08:01 UTC

## 📊 cuspide.fr

- **Rapports reçus** : 9
- **Volume emails** : 357
- **Conformité DMARC** : 27.7% (99/357)
  - ✅ DKIM + SPF tous deux OK : 91 (25.5%)
  - ✅ DKIM seul OK (forwarding) : 4 (1.1%)
  - ✅ SPF seul OK : 4 (1.1%)
  - 🚨 DKIM + SPF tous deux FAIL : 258 (72.3%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `209.85.220.41` | 262 | Google / Gmail forwarder | ⚠️ 1.5% |
| `212.227.126.135` | 7 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 7 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 7 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 6 | IONOS Mail SMTP | ✅ 100.0% |
| `54.240.3.27` | 5 | Amazon SES (Resend / app) | ✅ 100.0% |
| `212.227.17.24` | 5 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.187` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `54.240.6.53` | 3 | Amazon SES (Resend / app) | ✅ 100.0% |
| `54.240.3.30` | 3 | Amazon SES (Resend / app) | ✅ 100.0% |
| `54.240.3.25` | 3 | Amazon SES (Resend / app) | ✅ 100.0% |
| `54.240.3.15` | 3 | Amazon SES (Resend / app) | ✅ 100.0% |
| `54.240.3.13` | 3 | Amazon SES (Resend / app) | ✅ 100.0% |
| `217.72.192.74` | 3 | IONOS Mail SMTP | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `209.85.220.41` | 258 | Google / Gmail forwarder | `gmail.com` | `—` |

> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation.

---

## 📊 kelaj-company.com

- **Rapports reçus** : 3
- **Volume emails** : 7
- **Conformité DMARC** : 100.0% (7/7)
  - ✅ DKIM + SPF tous deux OK : 0 (0.0%)
  - ✅ DKIM seul OK (forwarding) : 7 (100.0%)
  - ✅ SPF seul OK : 0 (0.0%)
  - 🚨 DKIM + SPF tous deux FAIL : 0 (0.0%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `212.227.126.133` | 2 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 2 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 1 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 1 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 1 | IONOS Mail SMTP | ✅ 100.0% |

---

## 📊 news.cuspide.fr

- **Rapports reçus** : 9
- **Volume emails** : 129
- **Conformité DMARC** : 96.9% (125/129)
  - ✅ DKIM + SPF tous deux OK : 110 (85.3%)
  - ✅ DKIM seul OK (forwarding) : 14 (10.9%)
  - ✅ SPF seul OK : 1 (0.8%)
  - 🚨 DKIM + SPF tous deux FAIL : 4 (3.1%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `217.72.192.73` | 13 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.187` | 13 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 13 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 12 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 12 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 11 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 10 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 7 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 7 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 5 | IONOS Mail SMTP | ✅ 100.0% |
| `35.174.145.124` | 4 | Inconnu | 🚨 0.0% |
| `217.72.192.75` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `209.85.220.69` | 3 | Google / Gmail forwarder | ✅ 100.0% |
| `209.85.220.41` | 3 | Google / Gmail forwarder | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `35.174.145.124` | 4 | Inconnu | `news.cuspide.fr` | `news.cuspide.fr` |

> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation.

---

## 📊 pros.kelaj-company.com

- **Rapports reçus** : 10
- **Volume emails** : 103
- **Conformité DMARC** : 100.0% (103/103)
  - ✅ DKIM + SPF tous deux OK : 94 (91.3%)
  - ✅ DKIM seul OK (forwarding) : 9 (8.7%)
  - ✅ SPF seul OK : 0 (0.0%)
  - 🚨 DKIM + SPF tous deux FAIL : 0 (0.0%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `212.227.126.135` | 13 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 12 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 12 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 9 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 9 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 9 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 8 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 7 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 5 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 5 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 5 | IONOS Mail SMTP | ✅ 100.0% |
| `20.4.48.55` | 3 | Inconnu | ✅ 100.0% |
| `20.4.48.52` | 2 | Inconnu | ✅ 100.0% |
| `20.4.48.48` | 2 | Inconnu | ✅ 100.0% |
| `20.4.48.53` | 1 | Inconnu | ✅ 100.0% |

---
