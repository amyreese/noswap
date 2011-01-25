title: Games
menu-position: 4
sig:
---

{%
pages = pagelist(key=lambda p: p.get("menu-parent") == page["menu-position"], sortby=lambda p: p.get("title"))
for p in pages:
	print "*   [%s](%s)" % (p.title, p.url)
	subpages = pagelist(key=lambda sp: sp.get("menu-parent") == p["menu-position"], sortby=lambda sp: sp.get("title"))
	for sp in subpages:
		print "    *   [%s](%s)" % (sp.title, sp.url)
%}
