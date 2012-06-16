
# Copyright (C) 2010 John Reese
# Licensed under the MIT license

poole=./poole.py

archives=$(shell find input/blog/ -mindepth 2 -regex '.*/[0-9]+/index.md')
tags=$(shell find input/blog/tag/ -mindepth 1 -name 'index.md' -prune -o -print)

srcfiles=$(filter-out $(archives) $(tags),$(shell find input/))

puburi=liara:/srv/www/noswap/
previewuri=liara:/srv/www/noswap-preview/

.PHONY:
build: .output .presentation .content

.content: .output page.html macros.py $(srcfiles)
	$(poole) --build --ignore '^\.|~$$|\.ccss$$|\.swp$$'
	touch .content

.presentation: .output .content main.less
	lessc main.less > output/css/main.css
	touch .presentation

.PHONY:
preview: build
	rsync -avz --delete output/ $(previewuri)

.PHONY:
publish: build
	rsync -avz --delete output/ $(puburi)

.PHONY:
clean:
	rm -rf output/ macros.pyc $(archives) $(tags) .build .presentation .output

.PHONY:
fresh: clean build

.output:
	mkdir output/
	touch .output

