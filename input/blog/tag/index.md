title: Tags
rel:
---
{%
tags = []
pages = pagelist(key=lambda p: p.get("tags"))
for p in pages:
	tags.extend(tagsplit.findall(p.tags))

tags = list(set(tags))
tags.sort()

for tag in tags:
	print "*	[%s](%s)" % (tag, "/blog/tag/%s/" % tag.replace(" ", "-"))
%}
