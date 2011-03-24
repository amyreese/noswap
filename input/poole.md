title: Generated using Poole
---
The structure of this website is generated using [Poole][], a software project
by Oben Sonne.  Pages are written using [Markdown syntax][markdown], and then
compiled into a static HTML website.

The source code (and content) for generating this site is open source, using a
combination of MIT license for the code and a Creative Commons license for the
actual website content.  You can browse the [repository on GitHub][1], and you
can use the source code as a starting point to generate your own web site.

You will need to install [Poole][] and its dependencies using instructions
from the project's webpage, and then clone the repository.  Once you've
cloned the repository, building the website is just a matter of running `make`
from the repository's root directory.

The Poole macros defined in `macros.py` will automatically generate archive
pages as needed for pages with the "date:" metadata defined in the format of
"YYYY-MM-DD", and will create archive pages as `blog/YYYY/MM/index.md`. For
pages with the "tags:" metadata as a list of comma-separated tag names, a macro
will create tag pages as `blog/tag/<name>.md`.

Regarding URLs, `macros.py` and `.htaccess` generate "pretty" URL schemes that
hide the .html file extension, and automatically add a trailing slash.  If you
don't like this, you'll need to modify both files.

Happy hacking.

[markdown]: http://daringfireball.net/projects/markdown/syntax "Markdown"
[poole]: http://bitbucket.org/obensonne/poole/src "Poole"

[1]: http://github.com/jreese/noswap "NoSwap repo on GitHub"
