
import clevercss
import glob
import os
from os import path
import re

page = {
	"logo": "LeetCode.net",
	"logo-url": "/",
	"tagline": "open source software engineering",
	}

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

def once_htaccess():
	fi = open(os.path.join(input, ".htaccess"))
	fo = open(os.path.join(output, ".htaccess"), "w")
	fo.writelines(fi.readlines())
	fi.close()
	fo.close()
