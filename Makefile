poole=$(shell which poole)

.PHONY: build
build: output
	$(poole) --build --ignore '^\.|~$$|\.swp$$|\.ccss$$'

.PHONY: serve
serve: build
	-$(poole) --serve

output:
	mkdir output
