
# Copyright (C) 2010 John Reese
# Licensed under the MIT license

puburi=liara:/srv/www/noswap/
previewuri=liara:/srv/www/noswap-preview/

.PHONY:
preview: clean
	nib --debug --config preview.nib
	rsync -avz --delete site/ $(previewuri)

.PHONY:
publish: clean
	nib --debug
	rsync -avz --delete site/ $(puburi)

.PHONY:
clean:
	rm -rf site/

