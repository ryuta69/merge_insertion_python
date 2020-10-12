build:
	poetry install

annotate:
	poetry run monkeytype run __main__.py
	poetry run monkeytype list-modules

typecheck:
	poetry run mypy --strict-optional --disallow-untyped-defs --disallow-untyped-calls ./src

format:
	poetry run isort ./src
	poetry run black ./src

lint:
	poetry run flake8 ./src --ignore=E501,E203,W503 --max-line-length=120 --show-source

test:
	poetry run pytest --capture=no --verbose ./src/test
