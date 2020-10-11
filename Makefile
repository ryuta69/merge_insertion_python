build:
	poetry install

typecheck:
	poetry run pytype ./src

format:
	poetry run isort ./src && poetry run black ./src

lint:
	poetry run flake8 ./src --ignore=E501,E203,W503 --max-line-length=120 --show-source
