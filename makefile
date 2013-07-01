
# Copyright (C) 2010 John Reese
# Licensed under the MIT license

puburi=liara:/srv/www/noswap/
previewuri=liara:/srv/www/noswap-preview/

.PHONY:
previewbuild:
	nib --debug --config preview.nib build

.PHONY:
build:
	nib --debug build

.PHONY:
preview: clean previewbuild
	rsync -avz --delete site/ $(previewuri)

.PHONY:
publish: clean build
	rsync -avz --delete site/ $(puburi)

.PHONY:
clean:
	rm -rf site/

