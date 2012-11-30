title:
notitle:
menu-position: 2
menu-title: Blog
sig:
rel:
---
{%
posts = pagelist(key=lambda p: p.get("date"), sortby=lambda p: p.get("date"), reverse=True, limit=15)
for p in posts:
	inline(p)
%}

<p class="more">Read more in the <a href="/blog/archive/">archive</a> ...</p>
