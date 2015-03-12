
# Copyright (C) 2010 John Reese
# Licensed under the MIT license

puburi=liara:/srv/www/noswap/

bootstrap=third-party/bootstrap

.PHONY:
local: bootstrap
	nib --debug --config local.nib build

.PHONY:
public: bootstrap
	nib --debug build

.PHONY:
publish: clean public
	rsync -avz --delete site/ $(puburi)

.PHONY:
bootstrap: resources/css/bootstrap.min.css resources/js/bootstrap.min.js
	cd $(bootstrap) && git checkout -f

resources/css/bootstrap.min.css: resources/css/variables.less
	cp $< $(bootstrap)/less/variables.less
	cd $(bootstrap) && grunt dist
	cp $(bootstrap)/dist/css/bootstrap.min.css $@

resources/css/bootstrap-theme.min.css: resources/css/variables.less
	cp $(bootstrap)/dist/css/bootstrap-theme.min.css $@

resources/js/bootstrap.min.js: resources/css/variables.less
	cp $(bootstrap)/dist/js/bootstrap.min.js $@

.PHONY:
clean:
	rm -rf site/

