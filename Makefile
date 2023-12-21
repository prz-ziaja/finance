test-local:
	pytest src/tests && black --check src && isort --check srciso