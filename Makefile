poole=$(shell which poole)
markdownpp=$(shell which markdown-pp)

mdpp=$(shell find input/ -name '*.mdpp')
md=$(patsubst %.mdpp,%.md,$(mdpp))

archives=$(shell find input/blog/ -mindepth 2 -regex '.*/[0-9]+/index.md')
tags=$(shell find input/blog/tag/ -mindepth 1 -name 'index.md' -prune -o -print)

puburi=jreese@dyson:/srv/www/sites/leetcode.net/pages/

.PHONY: build
build: output $(md)
	$(poole) --build --ignore '^\.|~$$|\.ccss$$|\.mdpp$$|\.swp$$'

.PHONY: publish
publish: fresh
	rsync -avz --delete output/ $(puburi)

.PHONY: serve
serve: build
	-$(poole) --serve

.PHONY: clean
clean:
	rm -rf output/ macros.pyc $(md) $(archives) $(tags)

.PHONY: fresh
fresh: clean build

output:
	mkdir output/

%.md : %.mdpp
	$(markdownpp) $< $@

