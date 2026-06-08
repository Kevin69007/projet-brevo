---
name: Audit DNS dig avant warmup
description: Avant de capitaliser "DNS OK" ou de lancer un warmup email, toujours dig SPF+DKIM+DMARC réellement
type: feedback
originSessionId: b99f8f53-147b-41ab-96a7-bc601217366f
---
Avant de lancer un warmup mailbox (Allegrow/Neverspam/autre) ou de capitaliser dans un bilan que "DNS OK", **toujours vérifier en réel** via `dig` :

```bash
dig +short TXT <domaine>                                     # SPF
for s in s1 s2 ionos default selector1 selector2 dkim k1 mail brevo; do
  r=$(dig +short TXT ${s}._domainkey.<domaine>); [ -n "$r" ] && echo "$s: $r"
done                                                          # DKIM (multi-sélecteurs)
dig +short TXT _dmarc.<domaine>                              # DMARC
dig +short TXT _dmarc.<parent_domain>                        # DMARC parent
```

**Why:** Sur news.cuspide.fr, le bilan du 26/03/2026 écrivait "SPF ✅ DKIM ✅ DMARC ✅". Audit du 05/05 (40 jours après) : DKIM totalement absent, DMARC absent, DMARC parent avec `rua=mailto:postmaster@exemple.com` (placeholder doc jamais corrigé). Résultat : 40j de warmup brûlés, spam rate 58%, étape 7+ du projet Brevo bloquée. Gmail/Yahoo (politique 02/2024) classent automatiquement les emails non signés DKIM en spam.

**How to apply:**
- Avant tout warmup → audit `dig` complet, pas juste "j'ai cliqué Activer DKIM dans le panel"
- Avant d'écrire "DNS OK" dans un projet/bilan → `dig` puis copier la valeur réelle dans le doc
- Si DMARC contient `mailto:postmaster@exemple.com` ou autre placeholder doc → considérer le record cassé
- Vérifier aussi le DMARC du **domaine parent** (les sous-domaines héritent partiellement)
- Côté IONOS : activer DKIM dans le panel ne suffit pas toujours — vérifier que le record TXT est bien publié dans la zone DNS
