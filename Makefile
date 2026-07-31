.PHONY: generate validate manifest package

PYTHON ?= python3

generate:
	$(PYTHON) tools/generate_compendium.py

validate:
	$(PYTHON) tools/validate.py

manifest:
	$(PYTHON) tools/update_manifest.py

package: generate manifest validate
	$(PYTHON) tools/package.py
