.PHONY: docs docs-serve evaluate generate test validate validate-normative manifest package resolve

PYTHON ?= python3

generate:
	$(PYTHON) tools/generate_compendium.py

docs:
	$(PYTHON) tools/generate_site_docs.py
	mkdocs build

docs-serve:
	$(PYTHON) tools/generate_site_docs.py
	mkdocs serve

test:
	$(PYTHON) -m unittest discover -s tests -p 'test_*.py'

evaluate:
	$(PYTHON) tools/evaluate.py

validate:
	$(PYTHON) tools/validate.py $(VALIDATE_FLAGS)
	$(MAKE) evaluate PYTHON=$(PYTHON)
	$(MAKE) test PYTHON=$(PYTHON)

validate-normative:
	$(PYTHON) tools/validate.py --lint-normative

manifest:
	$(PYTHON) tools/update_manifest.py

package: generate manifest validate
	$(PYTHON) tools/package.py

resolve:
	$(PYTHON) tools/orchestrate.py --repository . $(RESOLVE_FLAGS)
