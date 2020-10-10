build:
	pyflow sync

format:
	pyflow flake8 ./src --ignore=E203,W503 --show-source

lint:
	pyflow black ./src
