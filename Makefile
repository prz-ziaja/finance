test-local:
	pytest src/tests && black --check src && isort --check src

prepare:
	pytest src/tests && black  src && isort src