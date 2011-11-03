title:
notitle:
sig:
rel:
---
{%
posts = pagelist(key=lambda p: p.get("date"), sortby=lambda p: p.get("date"), reverse=True, limit=15)
for p in posts:
	inline(p)
%}

