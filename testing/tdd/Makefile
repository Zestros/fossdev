create-structure:
	mkdir src
	mkdir tests
	mkdir docs
	touch README.md
	touch setup.py
	touch requirement.txt
	touch docs/DOMAIN.md
	touch src/.gitkeep tests/.gitkeep

venv:
	python3 -m venv .venv
install-dep: venv
	. .venv/bin/activate && pip install -r requirement.txt

install: install-dep
	. .venv/bin/activate && pip install -e .

test-pytest:
	. .venv/bin/activate && python -m pytest

test: venv install-dep install test-pytest

clean:
	rm -rf .venv
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
