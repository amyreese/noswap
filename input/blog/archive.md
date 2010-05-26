title: Archive
menu-position: 9
---
{%
pages = pagelist(key=lambda p: p.get("menu-parent") == page["menu-position"], sortby=lambda p: p.get("url"), reverse=True)
for p in pages:
	print "*	[%s](%s)" % (p.title, p.url)
%}
