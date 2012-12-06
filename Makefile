
# Copyright (C) 2010 John Reese
# Licensed under the MIT license

puburi=liara:/srv/www/noswap/
previewuri=liara:/srv/www/noswap-preview/

.PHONY:
build:
	nib --debug

.PHONY:
preview: build
	rsync -avz --delete site/ $(previewuri)

.PHONY:
publish: build
	rsync -avz --delete site/ $(puburi)

.PHONY:
clean:
	rm -rf site/

.PHONY:
fresh: clean build

