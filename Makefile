# Makefile
setup:
	poetry install

update:
	poetry update

export:
	poetry export -f requirements.txt --output requirements.txt
	poetry export -f requirements.txt --output requirements-dev.txt --only dev

run:
	poetry run uvicorn src.app.main:app --reload

test:
	poetry run pytest

test-verbose:
	poetry run pytest -vss
