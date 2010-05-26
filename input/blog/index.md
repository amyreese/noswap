title:
menu-position: 1
menu-title: Blog
---
{%
posts = pagelist(key=lambda p: p.get("date"), sortby=lambda p: p.get("date"), reverse=True)
for p in posts:
	inline(p)
%}

