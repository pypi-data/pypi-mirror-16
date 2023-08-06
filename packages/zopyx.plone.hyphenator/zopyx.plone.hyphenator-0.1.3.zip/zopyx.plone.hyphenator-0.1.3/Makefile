release: build
	mkrelease -p -d pypi

build:
	cd zopyx/plone/hyphenator/browser/resources; make; git commit -m updated js-compiled-min.js; git push
