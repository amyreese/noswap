
# Copyright (C) 2010 John Reese
# Licensed under the MIT license

puburi=liara:/srv/www/noswap/

.PHONY:
local:
	nib --debug --config local.nib build

.PHONY:
public:
	nib --debug build

.PHONY:
publish: clean public
	rsync -avz --delete site/ $(puburi)

.PHONY:
clean:
	rm -rf site/

