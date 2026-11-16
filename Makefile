VENV = $(HOME)/goinfre/.venv
CACHE = $(HOME)/goinfre/.cache/uv
ADD ?=

export UV_CACHE_DIR = $(CACHE)
export UV_PROJECT_ENVIRONMENT = $(VENV)

install:
	@uv sync

add:
	@uv add $(ADD)

run: install
	@uv run call-me-maybe
