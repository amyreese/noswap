poole=$(shell which poole)
markdownpp=$(shell which markdown-pp)

mdpp=$(shell find input/ -name '*.mdpp')
md=$(patsubst %.mdpp,%.md,$(mdpp))

archives=$(shell find input/blog/ -mindepth 2 -name 'index.md')

.PHONY: build
build: output $(md)
	$(poole) --build --ignore '^\.|~$$|\.ccss$$|\.mdpp$$|\.swp$$'

.PHONY: serve
serve: build
	-$(poole) --serve

.PHONY: clean
clean:
	rm -rf output/ macros.pyc $(md) $(archives)

.PHONY: fresh
fresh: clean build

output:
	mkdir output/

%.md : %.mdpp
	$(markdownpp) $< $@

