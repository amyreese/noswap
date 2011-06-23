title: Articles
menu-position: 2
sig:
---
{%
posts = pagelist(key=lambda p: "tags" in p and "article" in tagsplit.findall(p.tags), sortby=lambda p: p.get("date"), reverse=True)
for p in posts:
	print "*	[%s](%s)" % (p.title, pretty(p.url))
%}
