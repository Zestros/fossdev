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
	@echo "make check-requirements Checking all dependencies"
	@echo "typecheck               Type checking"

$(VENV)/bin/python:
	python3 -m venv $(VENV)

run:
	$(PYTHON) $(SRC)/app.py

venv: $(VENV)/bin/python

install: $(VENV)/bin/python requirements.txt
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

check-requirements: install
	$(PYTHON) sub_scripts/check_requirements.py

typecheck: install
	$(PYTHON) -m mypy $(SRC)

