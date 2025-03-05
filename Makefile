.venv: uv.lock
	uv sync
	touch -c .venv

init: .venv

# Run the tests once
test:
	uv run pytest
.PHONY: test

# Avoid any network calls, just test harness
test-local:
	uv run pytest -m local

# Run pytest in watch mode using pytest-watcher (ptw)
watch:
	uv run pytest-watcher --now . -- --testmon
.PHONY: watch 

clean:
	rm -rf .venv .pytest_cache .ruff_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +

.PHONY: clean

format:
	uv run ruff format
.PHONY: format
