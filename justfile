
test:
    uv run pytest tests/

format:
    ruff format

dist:
    rm -rf dist
    uv build

publish: dist
    uv publish
