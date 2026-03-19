create-structure:
	mkdir src
	mkdir tests
	mkdir docs
	touch README.md
	touch setup.py
	touch requirement.txt
	touch docs/DOMAIN.md
	touch src/.gitkeep tests/.gitkeep

install-dep:
	pip install -r requirement.txt

install:
	pip install -e .

test-pytest:
	python -m pytest

test: install-dep install test-pytest