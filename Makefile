VENV = $(HOME)/goinfre/.venv
CACHE = $(HOME)/goinfre/.cache/uv
ADD ?=
FUNCTIONS ?= data/input/functions_definition.json
INPUT ?= data/input/function_calling_tests.json
OUTPUT ?= data/output/function_calls.json

export UV_CACHE_DIR = $(CACHE)
export UV_PROJECT_ENVIRONMENT = $(VENV)

install:
	@uv sync

add:
	@uv add $(ADD)

run: install
	@uv run -m src --functions_definition $(FUNCTIONS) --input $(INPUT) --output $(OUTPUT)

clean:
	rm -rf $(VENV)
	rm -rf $(CACHE)
	rm -rf src/__pycache__

lint:
	@uv run -m flake8 . --exclude llm_sdk
