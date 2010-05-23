poole=$(shell which poole)

.PHONY: build
build:
	$(poole) --build --ignore '^\.|~$$|\.swp$$|\.ccss$$'

.PHONY: serve
serve: build
	-$(poole) --serve

