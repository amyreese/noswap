title: Articles
menu-position: 2
sig:
rel:
---
{%
posts = pagelist(key=lambda p: "tags" in p and "article" in tagsplit.findall(p.tags), sortby=lambda p: p.get("date"), reverse=True)
for p in posts:
	inline(p)
%}
