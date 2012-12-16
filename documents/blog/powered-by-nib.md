title: Powered by Nib
description: In which I describe my latest project and how this site now uses it.
date: 2012-12-15
tags: me, nib
---
For the last couple years, this site has been managed and updated using the open
source static site generator called [Poole][].  It is an excellent and simple
system, comprised of two Python files -- the Poole source code and a
site-specific [macros.py][] -- a simple page template, input documents and
static content.  This is more than enough for a small static website, but
more complicated sites, like blogs, require quite a few macros in order to
generate things like archives, tag pages, or even RSS feeds.  Over the 18
months that I worked with Poole, my macro file had gotten a bit disorganization,
and the limitation of working from only a single template file was starting to
strain on what I could do with it.

Now keep in mind, I still like many of the features that drew me to Poole in the
first place, such as the use of a document-centric build process, with YAML
headers for defining page metadata rather than an inline, proprietary format
used by projects like Jekyll.  I also enjoy the simplicity of the content
representations, but the lack of an extensible content pipeline is my biggest
complaint.  Supporting formats other than Markdown requires adding yet another
hook to the macro file; generating archives and tag pages required hacking in a
multi-phase build using `os.exec()`; and inlining another page's content
post-render was just not possible, resulting in Markdown named-link collisions
when rendering multiple posts to a single page.

I wanted something new.  So, for the past few months, I've been working on
[Nib][].

The resulting design is based heavily on the concepts of Poole, but built
around a primary goal of producing a proper content pipeline that is
simultaneously aware of the differentiation between resources and documents, and
defines multiple stages where plugins can hook into the process and alter or
generate page contents at build time.  Indeed, most of the actual functionality
of Nib is contained within a handful of plugins, while the main module merely
defines a framework for the content pipeline.

In effect, adding support for more content or resource formats should be as
simple as adding a new plugin attached to the appropriate file extensions.
Advanced content manipulation, generating "virtual pages", and aggregating
pages or documents into multiple locations are all possible as well.

The Markdown plugin is 14 lines of code; the LessCSS plugin is 13; even the
blog plugin -- which generates the archive pages, tag listings, and Atom feed --
takes only 86 lines to do a better job than the old Poole macros that required
double the effort.

Nib is still in an extremely early, and unstable, phase though.  It works for
the needs of my site, and does come with some basic documentation and a
[sample site][] to start from, but it's far from complete.  Near term goals
include adding support for an intelligent menu, as well as support for more
content and resource formats, like reStructuredText or SASS.  Contributions are
always welcome though, even at this early stage.  Nib is liberally licensed,
and I would love to hear feedback from anyone trying to use it.  Hopefully it
will be useful for someone other than myself.


[poole]: http://bitbucket.org/obensonne/poole/src
[macros.py]: https://github.com/jreese/noswap/blob/poole/macros.py
[nib]: https://github.com/jreese/nib
