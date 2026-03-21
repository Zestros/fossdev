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

$(VENV)/bin/python:
	python3 -m venv $(VENV)

venv: $(VENV)/bin/python

install: $(VENV)/bin/python requirements.txt
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
