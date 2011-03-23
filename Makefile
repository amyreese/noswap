
# Copyright (C) 2010 John Reese
# Licensed under the MIT license

poole=$(shell which poole)
markdownpp=$(shell which markdown-pp)

archives=$(shell find input/blog/ -mindepth 2 -regex '.*/[0-9]+/index.md')
tags=$(shell find input/blog/tag/ -mindepth 1 -name 'index.md' -prune -o -print)

mdppfiles=$(shell find input/ -name '*.mdpp')
mdfiles=$(patsubst %.mdpp,%.md,$(mdppfiles))

srcfiles=$(filter-out $(archives) $(tags) $(mdfiles),$(shell find input/))

puburi=dyson:/srv/www/sites/noswap/pages/

build: .build

.build: output page.html macros.py $(srcfiles) $(mdfiles)
	$(poole) --build --ignore '^\.|~$$|\.ccss$$|\.mdpp$$|\.swp$$'
	touch .build

.PHONY:
publish: build
	rsync -avz --delete output/ $(puburi)

.PHONY:
serve: build
	-$(poole) --serve

.PHONY:
clean:
	rm -rf output/ macros.pyc $(mdfiles) $(archives) $(tags) .build

.PHONY:
fresh: clean build

output:
	mkdir output/

%.md : %.mdpp
	$(markdownpp) $< $@

