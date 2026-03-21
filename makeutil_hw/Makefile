.DEFAULT_GOAL := help

VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
SRC := src

.PHONY: help install

help:
	@echo "Commands:"
	@echo "make venv               Create venv"
	@echo "make install            Install dependencies"
    @echo "make check-requirements Checking all dependencies"

$(VENV)/bin/python:
	python3 -m venv $(VENV)

venv: $(VENV)/bin/python

install: check-requirements
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

check-requirements: $(VENV)/bin/python requirements.txt
	$(PYTHON) sub_scripts/check_requirements.py