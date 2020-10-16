build:
	poetry install

test:
	poetry run pytest

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

doc:
	# poetry run sphinx-quickstart docs
	# # add 'sphinx.ext.autodoc', 'sphinx.ext.napoleon' in conf.py
	poetry run sphinx-apidoc -f -o ./docs .
	poetry run sphinx-build -b singlehtml ./docs ./docs/_build

all: test annotate typecheck format lint
