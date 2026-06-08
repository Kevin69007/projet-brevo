# DNS Records — Par Domaine

> Derniere MAJ : 5 mai 2026 (post-fix DNS news.cuspide.fr)
> Registrar : IONOS | API : `claude-dns` key
> DNS gere via API IONOS — POST pour creer, PUT pour update record existant
> Zone cuspide.fr ID : `6a9b6398-2cf9-11ec-bda4-0a5864441f49`

## news.cuspide.fr — ACTIF (sous-domaine principal pour envoi)

### Statut : ✅ DNS authentification complete (05/05/2026)
### Mode envoi actuel : **IONOS SMTP via mailbox** (pour warmup Allegrow)
### Mode envoi futur (campagnes) : Brevo (records Brevo a ajouter quand campagnes demarrent)

| Record | Type | Name | Value | Statut |
|--------|------|------|-------|--------|
| SPF | TXT | news.cuspide.fr | `v=spf1 include:_spf-eu.ionos.com ~all` | ✅ IONOS only |
| MX | MX | news.cuspide.fr | mx00/mx01.ionos.fr | ✅ |
| DKIM s1-ionos | CNAME | s1-ionos._domainkey.news.cuspide.fr | `s1.dkim.ionos.com` | ✅ |
| DKIM s2-ionos | CNAME | s2-ionos._domainkey.news.cuspide.fr | `s2.dkim.ionos.com` | ✅ |
| DKIM s42582890 (dyn) | CNAME | s42582890._domainkey.news.cuspide.fr | `s42582890.dkim.ionos.com` | ✅ ajoute 05/05 |
| DMARC | TXT | _dmarc.news.cuspide.fr | `v=DMARC1; p=none; pct=100; rua=mailto:dmarc@cuspide.fr; ruf=mailto:dmarc@cuspide.fr; aspf=r; adkim=r` | ✅ ajoute 05/05 |

### A faire plus tard (quand campagnes Brevo demarrent depuis news.cuspide.fr)
- Ajouter SPF Brevo : remplacer SPF actuel par `v=spf1 include:_spf-eu.ionos.com include:spf.brevo.com ~all`
- Ajouter TXT verification Brevo : `brevo-code:<code>` sur news.cuspide.fr
- Ajouter DKIM Brevo : `mail._domainkey.news.cuspide.fr` (TXT avec cle publique fournie par Brevo a l'auth domaine)
- Reference : voir laboratoire.cuspide.fr qui a la config Brevo complete

### Progression DMARC prevue (apres warmup OK)
- S1-4 (maintenant) : `p=none` — observer rapports
- S5-6 : `p=quarantine; pct=10`
- S7+ : `p=quarantine; pct=100` puis `p=reject`

## cuspide.fr — DOMAINE PARENT (touchable avec precaution)

⚠️ **cuspide.fr est en production pour toute l'equipe (redirection IONOS → Gmail)**

| Record | Value | Note |
|--------|-------|------|
| MX | mx00/mx01.ionos.fr | Email equipe via IONOS → Gmail |
| SPF | `v=spf1 include:_spf-eu.ionos.com ~all` | IONOS uniquement |
| DKIM | s1-ionos, s2-ionos, s42582890 (CNAME → ionos.com) | IONOS DKIM (les 3 selecteurs OK) |
| DMARC | `v=DMARC1; p=none; pct=100; rua=mailto:dmarc@cuspide.fr; ruf=mailto:dmarc@cuspide.fr` | ✅ corrige 05/05 (avant : placeholder bidon) |
| A | 217.160.0.216 | Site web IONOS |

### Sous-domaines cuspide.fr existants (ne pas toucher sans raison)
- **tutti.cuspide.fr** : App interne (Lovable) → 185.158.133.1
- **laboratoire.cuspide.fr** : Ancien Brevo (authentifie, SPF+DKIM+DMARC complets)
- **lien.cuspide.fr** : CNAME → links.switchy.io
- **prothese.cuspide.fr** : CNAME → quiz-proxy.marquiz.io
- **interne-traducteur.cuspide.fr** : CNAME → Railway

## Anciens domaines — EN QUARANTAINE (ne plus utiliser pour envoi)

### besmilecare.fr
- SPF : ✅ (IONOS + Brevo)
- DKIM : ❌ absent
- DMARC : ✅
- Allegrow : monitoring passif uniquement

### jak-company.com — SUPPRIME d'Allegrow
### wei-wei.fr — SUPPRIME d'Allegrow
