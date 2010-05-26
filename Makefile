poole=$(shell which poole)
markdownpp=$(shell which markdown-pp)

mdpp=$(shell find . -name '*.mdpp')
md=$(patsubst %.mdpp,%.md,$(mdpp))

.PHONY: build
build: output $(md)
	$(poole) --build --ignore '^\.|~$$|\.ccss$$|\.mdpp$$|\.swp$$'

.PHONY: serve
serve: build
	-$(poole) --serve

output:
	mkdir output

%.md : %.mdpp
	$(markdownpp) $< $@

