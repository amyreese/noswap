# encoding=utf-8

import clevercss
from datetime import datetime
import email.utils
import glob
import os
from os import path
import re
import time

base_url = "http://localhost:8080"

defaults = {
	"author": "John Reese",
	"tags": "",

	"time": "12:00:00",

	"menu-parent": "",
	"menu-position": "",
	"menu-title": "",

	"logo": "LeetCode.net",
	"logo-url": "/",
	"tagline": "open source software engineering",
	}
page = dict(defaults)


### Recursive Menu Structure

def menu(parent=""):
	menupages = [p for p in pages if p["menu-position"] != "" and p["menu-parent"] == parent]
	if (len(menupages) > 0):
		print "<ul>"
		for p in menupages:
			title = p["menu-title"] if p["menu-title"] != "" else p["title"]
			print """<li><a href="%s">%s</a>""" % (pretty(p.url), p.title)
			menu(p["menu-position"])
			print "</li>"
		print "</ul>"

### Inline another page's content

inlineeom = re.compile("^---\s*$")
inlineexcerpt = re.compile("^<!-- excerpt -->\s*$")
def inline(page, title=True):
	if title:
		print "<h1><a href=\"%s\">%s</a></h1>" % (pretty(page.url), page.title)

	fi = open(page.fname)
	input = fi.readlines()
	fi.close()

	eom = False
	excerpt = False
	output = []
	for line in input:
		line = line.strip("\n")
		if not eom:
			if inlineeom.search(line):
				eom = True
				output = []
				continue

		if inlineexcerpt.search(line):
			if excerpt:
				break
			else:
				output = []
				continue

		output.append(line)

	for line in output:
		print line

	print ""

	timestamp = datetime.strptime(page.date, "%Y-%m-%d").strftime("%B %d, %Y")
	print """<div class="metadata">"""
	print """<span class="authored">Posted on %s by %s</span>""" % (timestamp, page.author) 

	if "tags" in page and page.tags:
		taglist = ", ".join(["""<a href="/blog/tag/%s">%s</a>""" % (t.strip(), t.strip()) for t in page.tags.split(",")])
		print u"""<span class="tagged">§ Tagged as %s</span>""" % (taglist)

	print """</div>"""

### Pretty URLs

prettyurl = re.compile("^(.+/)?([^/]+)\.html$")
def pretty(url):
	match = prettyurl.search(url)

	if match:
		file = match.group(2)

		if match.group(1) is None:
			if match.group(2) == "index":
				return "/"
			else:
				return "/%s/" % (file)
		else:
			dir = match.group(1).rstrip("/")

			if file == "index":
				return "/%s/" % dir
			else:
				return "/%s/%s/" % (dir, file)
	else:
		return url

### CleverCSS

def once_clevercss():
	print("Building CSS files...")
	for ccss in glob.glob(os.path.join(input, "css/**.ccss")):
		print("  %s" % (ccss))
		css = ccss[len(input):].lstrip("/")
		css = "%s.css" % os.path.splitext(css)[0]
		css = os.path.join(output, css)
		fpi = open(ccss)
		fpo = open(css, 'w')
		fpo.write(clevercss.convert(fpi.read()))
		fpi.close()
		fpo.close()

### copy .htaccess to output directory

def once_htaccess():
	fi = open(os.path.join(input, ".htaccess"))
	fo = open(os.path.join(output, ".htaccess"), "w")
	fo.writelines(fi.readlines())
	fi.close()
	fo.close()

### RSS feed generation

_RSS = """<?xml version="1.0"?>
<rss version="2.0">
<channel>
<title>%s</title>
<link>%s</link>
<description>%s</description>
<language>en-us</language>
<pubDate>%s</pubDate>
<lastBuildDate>%s</lastBuildDate>
<docs>http://blogs.law.harvard.edu/tech/rss</docs>
<generator>Poole</generator>
%s
</channel>
</rss>
"""

_RSS_ITEM = """
<item>
	<title>%s</title>
	<link>%s</link>
	<description>%s</description>
	<pubDate>%s</pubDate>
	<guid>%s</guid>
</item>
"""

def once_rss():
	items = []
	posts = [p for p in pages if "date" in p] # get all blog post pages
	posts.sort(key=lambda p: p.date, reverse=True)
	for p in posts:
		title = p.title
		link = "%s%s" % (base_url, pretty(p.url))
		desc = p.get("description", "")
		date = time.mktime(time.strptime("%s %s" % (p.date, p.time), "%Y-%m-%d %H:%M:%S"))
		date = email.utils.formatdate(date)
		items.append(_RSS_ITEM % (title, link, desc, date, link))

	items = "".join(items)

	# --- CHANGE THIS --- #
	title = defaults["logo"]
	link = "%s/blog/" % base_url
	desc = defaults["tagline"]
	date = email.utils.formatdate()

	rss = _RSS % (title, link, desc, date, date, items)

	fp = open(os.path.join(output, "feed.xml"), 'w')
	fp.write(rss)
	fp.close()

