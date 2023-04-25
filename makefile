
# Copyright (C) Amethyst Reese
# Licensed under the MIT license

puburi=noswap.com:/srv/www/noswap/

sources=theme/variables.less theme/theme.less

.venv:
	python3 -m venv --clear --upgrade-deps .venv
	.venv/bin/python -m pip install -Ur requirements.txt

.PHONY:
local: .venv
	.venv/bin/nib --debug --config local.nib build

.PHONY:
public: .venv
	.venv/bin/nib --debug build

.PHONY:
serve: local
	.venv/bin/nib serve

.PHONY:
publish: clean public
	rsync -avz --delete site/ $(puburi)

.PHONY:
clean:
	rm -rf .venv/ site/ $(resources)

