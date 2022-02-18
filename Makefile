help:
	@echo "flake8		Execute flake8"
	@echo "tests		Execute unit tests"

format:
	@black src/ tests/

format-check:
	@black src/ tests/ --check

flake8:
	@flake8 . --config=.flake8

tests:
	@./run_tests

.PHONY: flake8 tests
