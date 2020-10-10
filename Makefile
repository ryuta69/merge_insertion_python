build:
	poetry install

format:
	poetry run flake8 ./src --ignore=E203,W503 --show-source

lint:
	poetry run black ./src
