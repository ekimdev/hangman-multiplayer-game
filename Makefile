help:
	@echo "flake8		Execute flake8"

flake8:
	@flake8 . --config=.flake8

.PHONY: flake8
