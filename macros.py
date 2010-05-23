
page = {
	"tagline": "open source software engineering",
	}

### CleverCSS

import clevercss
import glob
import os.path

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

