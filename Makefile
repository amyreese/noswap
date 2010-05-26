poole=$(shell which poole)
markdownpp=$(shell which markdown-pp)

srcfiles=$(shell find input/ -name '*.md')
mdppfiles=$(shell find input/ -name '*.mdpp')
mdfiles=$(patsubst %.mdpp,%.md,$(mdppfiles))

archives=$(shell find input/blog/ -mindepth 2 -regex '.*/[0-9]+/index.md')
tags=$(shell find input/blog/tag/ -mindepth 1 -name 'index.md' -prune -o -print)

puburi=jreese@dyson:/srv/www/sites/leetcode.net/pages/

build: .build

.build: output $(srcfiles) $(mdfiles)
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

