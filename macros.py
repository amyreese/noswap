# encoding=utf-8

import clevercss
from datetime import datetime
import glob
import os
from os import path
import re

page = {
	"author": "John Reese",
	"tags": "",

	"logo": "LeetCode.net",
	"logo-url": "/",
	"tagline": "open source software engineering",
	}


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
