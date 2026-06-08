# Rapport DMARC — 7 derniers jours

> Période : 2026-05-15 → 2026-05-22 (UTC)
> Généré le : 2026-05-22 08:05 UTC

## 📊 cuspide.fr

- **Rapports reçus** : 7
- **Volume emails** : 244
- **Conformité DMARC** : 26.2% (64/244)
  - ✅ DKIM + SPF tous deux OK : 60 (24.6%)
  - ✅ DKIM seul OK (forwarding) : 2 (0.8%)
  - ✅ SPF seul OK : 2 (0.8%)
  - 🚨 DKIM + SPF tous deux FAIL : 180 (73.8%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `209.85.220.41` | 182 | Google / Gmail forwarder | ⚠️ 1.1% |
| `212.227.126.131` | 5 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.187` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `54.240.3.27` | 3 | Amazon SES (Resend / app) | ✅ 100.0% |
| `54.240.3.25` | 3 | Amazon SES (Resend / app) | ✅ 100.0% |
| `54.240.3.13` | 3 | Amazon SES (Resend / app) | ✅ 100.0% |
| `217.72.192.75` | 3 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 3 | IONOS Mail SMTP | ✅ 100.0% |
| `54.240.6.245` | 2 | Amazon SES (Resend / app) | ✅ 100.0% |
| `54.240.3.29` | 2 | Amazon SES (Resend / app) | ✅ 100.0% |
| `54.240.3.26` | 2 | Amazon SES (Resend / app) | ✅ 100.0% |
| `54.240.3.15` | 2 | Amazon SES (Resend / app) | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `209.85.220.41` | 180 | Google / Gmail forwarder | `gmail.com` | `—` |

> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation.

---

## 📊 kelaj-company.com

- **Rapports reçus** : 2
- **Volume emails** : 5
- **Conformité DMARC** : 100.0% (5/5)
  - ✅ DKIM + SPF tous deux OK : 0 (0.0%)
  - ✅ DKIM seul OK (forwarding) : 5 (100.0%)
  - ✅ SPF seul OK : 0 (0.0%)
  - 🚨 DKIM + SPF tous deux FAIL : 0 (0.0%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `212.227.126.133` | 2 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 1 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 1 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 1 | IONOS Mail SMTP | ✅ 100.0% |

---

## 📊 news.cuspide.fr

- **Rapports reçus** : 9
- **Volume emails** : 131
- **Conformité DMARC** : 96.9% (127/131)
  - ✅ DKIM + SPF tous deux OK : 112 (85.5%)
  - ✅ DKIM seul OK (forwarding) : 14 (10.7%)
  - ✅ SPF seul OK : 1 (0.8%)
  - 🚨 DKIM + SPF tous deux FAIL : 4 (3.1%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `217.72.192.74` | 14 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.135` | 13 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.187` | 12 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 12 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 11 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 11 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 11 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 8 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 8 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 5 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 5 | IONOS Mail SMTP | ✅ 100.0% |
| `35.174.145.124` | 4 | Inconnu | 🚨 0.0% |
| `209.85.220.41` | 4 | Google / Gmail forwarder | ✅ 100.0% |
| `217.72.192.75` | 3 | IONOS Mail SMTP | ✅ 100.0% |
| `209.85.220.69` | 2 | Google / Gmail forwarder | ✅ 100.0% |

### 🚨 Alertes — émetteurs avec DMARC FAIL

| Source IP | Volume | Identification | Domaine SPF | Domaine DKIM |
|---|---|---|---|---|
| `35.174.145.124` | 4 | Inconnu | `news.cuspide.fr` | `news.cuspide.fr` |

> ⚠️ Ces émetteurs envoient des emails se prétendant venir de ce domaine sans authentification valide. À identifier : service tiers légitime à autoriser, ou tentative d'usurpation.

---

## 📊 pros.kelaj-company.com

- **Rapports reçus** : 9
- **Volume emails** : 95
- **Conformité DMARC** : 100.0% (95/95)
  - ✅ DKIM + SPF tous deux OK : 86 (90.5%)
  - ✅ DKIM seul OK (forwarding) : 9 (9.5%)
  - ✅ SPF seul OK : 0 (0.0%)
  - 🚨 DKIM + SPF tous deux FAIL : 0 (0.0%)

### Top sources d'envoi (volume)

| Source IP | Volume | Identification | DMARC PASS |
|---|---|---|---|
| `212.227.126.135` | 12 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.10` | 10 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.134` | 10 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.75` | 9 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.74` | 8 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.24` | 8 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.17.13` | 8 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.130` | 7 | IONOS Mail SMTP | ✅ 100.0% |
| `217.72.192.73` | 6 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.133` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `212.227.126.131` | 4 | IONOS Mail SMTP | ✅ 100.0% |
| `20.4.48.55` | 3 | Inconnu | ✅ 100.0% |
| `20.4.48.52` | 2 | Inconnu | ✅ 100.0% |
| `20.4.48.48` | 2 | Inconnu | ✅ 100.0% |
| `20.4.48.53` | 1 | Inconnu | ✅ 100.0% |

---
