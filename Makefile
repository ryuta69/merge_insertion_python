build:
	poetry install

annotate:
	poetry run pyannotate -w --py3 ./src
	# poetry run monkeytype run entrypoint_monkeytype.py
	# poetry run monkeytype list-modules

typecheck:
	poetry run mypy ./src

format:
	poetry run isort ./src
	poetry run black ./src

lint:
	poetry run flake8 ./src

test:
	poetry run pytest
