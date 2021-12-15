help:
	@echo "flake8		Execute flake8"
	@echo "tests		Execute unit tests"

flake8:
	@flake8 . --config=.flake8

tests:
	@python -m unittest -vb

.PHONY: flake8 tests
