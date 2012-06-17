title: Archive
menu-position: 9
sig:
---
{%
pages = pagelist(key=lambda p: p.get("menu-parent") == page["menu-position"], sortby=lambda p: p.get("url"), reverse=True)
for p in pages:
	print "*	[%s](%s)" % (p.title, pretty(p.url))
%}

<h2>Tags</h2>
{%
tags = []
pages = pagelist(key=lambda p: p.get("tags"))
for p in pages:
    tags.extend(tagsplit.findall(p.tags))

tags = list(set(tags))
tags.sort()

for tag in tags:
    print "*    [%s](%s)" % (tag, "/blog/tag/%s/" % tag.replace(" ", "-"))
%}
