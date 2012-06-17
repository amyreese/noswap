# encoding=utf-8

# Copyright (C) 2010 John Reese
# Licensed under the MIT license

from datetime import datetime
import email.utils
import glob
import os
from os import path
import re
import sys
import time

base_url = "http://noswap.com"

defaults = {
    "author": "John Reese",
    "tags": "",

    "time": "12:00:00",

    "menu-parent": "",
    "menu-position": "",
    "menu-title": "",

    "crumb": "/",

    "logo": "NoSwap.com",
    "logo-url": "/",
    "tagline": "open source software engineering",

    "comments": "",
    "sig": """<p class="sig">&lambda;</p>""",
    "rel": "author",
    "link": "https://profiles.google.com/111348339961490289797",
    }
page = dict(defaults)

tagsplit = re.compile("(\w+(?:\s+\w+)*)")

### Recursive Menu Structure

def menu(page, parent="", id="", recursive=True):
    menupages = pagelist(
            key=lambda p: p["menu-position"] != "" and p["menu-parent"] == parent,
            sortby=lambda p: int(p.get("menu-position"))
            )
    if (len(menupages) > 0):
        if id == "":
            print "<ul>"
        else:
            print "<ul id=\"%s\">" % id

        for p in menupages:
            title = p["menu-title"] if p["menu-title"] != "" else p["title"]
            if page.url == p.url:
                print """<li><a class="current" href="%s">%s</a>""" % (pretty(p.url), title)
            else:
                print """<li><a href="%s">%s</a>""" % (pretty(p.url), title)
            if recursive:
                menu(page, parent=p["menu-position"])
            print "</li>"
        print "</ul>"

### Breadcrumb Navigation

def crumbs(page):
    if "notitle" in page:
        return

    if "nocrumbs" in page:
        print """<h1><a href="%s">%s</a></h1>""" % (pretty(page.url), page.title)
        return

    crumb_url = page.crumb
    url = pretty(page.url)
    if url.startswith(crumb_url):
        url = url.split(crumb_url, 1)[1]

    segments = url.split("/")

    more = False
    crumb_url = "/"

    print "<h1>"

    for segment in segments:
        if segment == "":
            continue

        crumb_url += segment + "/"
        pretty_url = pretty(crumb_url)

        matching_pages = [p for p in pages if pretty(p.url) == pretty_url and p.title]

        if len(matching_pages) > 0:
            title = matching_pages[0].title
            print """%s<a href="%s">%s</a>""" % (" &raquo; " if more else "", pretty_url, title)
            more = True

    print "</h1>"

### Post Retrieval

def pagelist(key=None, sortby=None, reverse=False, limit=None):
    if key is None:
        return []

    pagelist = [p for p in pages if key(p)]

    if sortby is None:
        pagelist.sort(key=lambda p: p.get("title"))
    else:
        pagelist.sort(key=sortby, reverse=reverse)

    if limit is None:
        return pagelist
    elif len(pagelist) > limit:
        return pagelist[0:limit]
    else:
        return pagelist

### Inline another page's content

inlineeom = re.compile("^---\s*$")
startexcerpt = re.compile("^<!-- excerpt -->\s*$")
endexcerpt = re.compile("^<!-- endexcerpt -->\s*$")
def inline(page, title=True):
    if title:
        print "<h2><a href=\"%s\">%s</a></h2>" % (pretty(page.url), page.title)
        metadata(page)

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

        if startexcerpt.search(line):
            output = []
            continue

        if endexcerpt.search(line):
            excerpt = True
            break

        output.append(line)

    for line in output:
        print line

    print ""

    if excerpt:
        print """<p class="excerpt"><a href="%s">Continue reading &raquo;</a></p>""" % pretty(page.url)
    else:
        print page.sig

### Page metadata display

def metadata(page, style="subtitle"):
    if style == "subtitle":
        if "date" in page:
            timestamp = datetime.strptime(page.date[0:10], "%Y-%m-%d").strftime("%B %d, %Y")

            print """<p class="metadata">"""
            print """<span class="authored">Posted by <a rel="%s" href="%s">%s</a> on %s</span>""" % (
                page.rel, page.link, page.author, timestamp)

            if "tags" in page and page.tags:
                tags = tagsplit.findall(page.tags)
                taglist = ", ".join(["""<a href="/blog/tag/%s/">%s</a>""" % (tag.replace(" ", "-"), tag) for tag in tags])
                print """<span class="tagged">&sect; Tagged as %s</span>""" % (taglist)

            print """</p>"""

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

### Livefyre comments

def livefyre():
    return """\
<!-- START: Livefyre Embed -->
<script type='text/javascript' src='https://www.livefyre.com/wjs/v1.0/javascripts/livefyre_init.js'></script>
<script type='text/javascript'>
    var fyre = LF({
        site_id: 289411,
        version: '1.0'
    });
</script>
<!-- END: Livefyre Embed -->
"""

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
    posts = pagelist(
            key=lambda p: "date" in p,
            sortby=lambda p: p.date,
            reverse=True,
            limit=5
            )
    for p in posts:
        title = p.title
        link = "%s%s" % (base_url, pretty(p.url))
        desc = p.get("description", "")
        date = time.mktime(time.strptime("%s %s" % (p.date[0:10], p.time), "%Y-%m-%d %H:%M:%S"))
        date = email.utils.formatdate(date)
        items.append(_RSS_ITEM % (title, link, desc, date, link))

    items = "".join(items)

    title = defaults["logo"]
    link = "%s/blog/" % base_url
    desc = defaults["tagline"]
    date = email.utils.formatdate()

    rss = _RSS % (title, link, desc, date, date, items)

    fp = open(os.path.join(output, "feed.xml"), 'w')
    fp.write(rss)
    fp.close()

### Auto-generate archive pages

def once_archive():
    datere = re.compile("(\d+)-(\d+)-\d+")
    archivetemplate = """title: %s
menu-parent: %s
menu-position: %s
nocrumbs:
sig:
rel:
---
{%%
posts = pagelist(key=lambda p: p.get("date", "").startswith("%s"), sortby=lambda p: p.get("date"), reverse=True)
for p in posts:
    inline(p)
%%}
"""

    generated = False
    menucount = 0

    blogpages = pagelist(key=lambda p: p.get("date"), sortby=lambda p: p.get("date"), reverse=True)
    for p in blogpages:
        url = pretty(p.url)

        match = datere.search(p.date)
        if match:
            year = match.group(1)
            month = match.group(2)

            date = datetime.strptime(p.date[0:10], "%Y-%m-%d")

            yeardir = path.join(input, "blog", year)
            if not path.exists(yeardir):
                os.mkdir(yeardir)

            yearfile = path.join(yeardir, "index.md")
            if not path.exists(yearfile):
                print "Generating %s ..." % yearfile

                fo = open(yearfile, "w")
                fo.write(archivetemplate % (year, "", "", year))
                fo.close()

                generated = True

            monthdir = path.join(yeardir, month)
            if not path.exists(monthdir):
                os.mkdir(monthdir)

            monthfile = path.join(monthdir, "index.md")
            if not path.exists(monthfile):
                print "Generating %s ..." % yearfile

                if menucount < 5:
                    parent = "9"
                    position = "9%d" % menucount
                    menucount += 1
                else:
                    parent = "9"
                    position = ""

                fo = open(monthfile, "w")
                fo.write(archivetemplate % (date.strftime("%B %Y"), parent, position, "%s-%s" % (year, month)))
                fo.close()

                generated = True

    if generated:
        print "Restarting build process..."
        os.execvp(sys.argv[0], sys.argv)

def once_tags():
    tagtemplate = """title: %s
sig:
rel:
---
{%%
posts = pagelist(key=lambda p: "tags" in p and "%s" in tagsplit.findall(p.tags), sortby=lambda p: p.get("date"), reverse=True)
for p in posts:
    inline(p)
%%}
"""

    generated = False
    tags = []

    blogpages = pagelist(key=lambda p: p.get("tags"))
    for p in blogpages:
        tags.extend(tagsplit.findall(p.tags))

    for tag in tags:
        tagfile = path.join(input, "blog", "tag", tag.replace(" ", "-")+".md")

        if not path.exists(tagfile):
            print "Generating %s ..." % tagfile

            fo = open(tagfile, "w")
            fo.write(tagtemplate % (tag, tag))
            fo.close()

            generated = True

    if generated:
        print "Restarting build process..."
        os.execvp(sys.argv[0], sys.argv)

