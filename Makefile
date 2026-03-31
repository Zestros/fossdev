.DEFAULT_GOAL := help

VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
SRC := src

.PHONY: help install run format lint typecheck check clean

help:
	@echo "Commands:"
	@echo "make venv               Create venv"
	@echo "make install            Install dependencies"
	@echo "typecheck               Type checking"
	@echo "format                  Format code in src"
	@echo "lint                    Lint code in src"
	@echo "check                   Check composition"

$(VENV)/bin/python:
	python3 -m venv $(VENV)

run: install
	$(PYTHON) $(SRC)/app.py

venv: $(VENV)/bin/python

install: $(VENV)/bin/python requirements.txt
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

typecheck: install
	$(PYTHON) -m mypy $(SRC)

format: install
	$(PYTHON) -m black $(SRC)

lint: install
	$(PYTHON) -m black --check $(SRC)

check: lint typecheck

clean:
	rm -rf $(VENV)