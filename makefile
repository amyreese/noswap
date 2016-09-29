
# Copyright (C) 2010 John Reese
# Licensed under the MIT license

puburi=kirby:/srv/www/noswap/

bootstrap=third-party/bootstrap
resources=resources/css/bootstrap.css resources/css/bootstrap.min.css resources/css/bootstrap-theme.css resources/css/bootstrap-theme.min.css resources/js/bootstrap.min.js
sources=theme/variables.less theme/theme.less

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
bootstrap: $(resources)
	cd $(bootstrap) && git checkout -f

resources/css/bootstrap.css: $(sources)
	cp $^ $(bootstrap)/less/
	cd $(bootstrap) && grunt dist
	cp $(bootstrap)/dist/css/bootstrap.css $@

resources/css/bootstrap.min.css: $(sources)
	cp $(bootstrap)/dist/css/bootstrap.min.css $@

resources/css/bootstrap-theme.css: $(sources)
	cp $(bootstrap)/dist/css/bootstrap-theme.css $@

resources/css/bootstrap-theme.min.css: $(sources)
	cp $(bootstrap)/dist/css/bootstrap-theme.min.css $@

resources/js/bootstrap.min.js: $(sources)
	cp $(bootstrap)/dist/js/bootstrap.min.js $@

.PHONY:
clean:
	rm -rf site/ $(resources)

