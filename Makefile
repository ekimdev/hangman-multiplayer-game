help:
	@echo "flake8		Execute flake8"
	@echo "tests		Execute unit tests"

flake8:
	@flake8 . --config=.flake8

tests:
	@./run_tests

.PHONY: flake8 tests
