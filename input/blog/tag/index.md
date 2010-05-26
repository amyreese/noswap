title: Tags
---
{%
tags = []
pages = pagelist(key=lambda p: p.get("tags"))
for p in pages:
	tags.extend(map(unicode.strip, p.tags.split(",")))

tags.sort()
for tag in tags:
	print "*	[%s](%s)" % (tag, "/blog/tag/%s/" % tag)
%}
