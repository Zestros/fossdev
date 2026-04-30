.DEFAULT_GOAL := help


create-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	mkdir -p $(PRACTICE)
	cp PracticeMakefile $(PRACTICE)/Makefile

remove-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	rm -rf $(PRACTICE)
	

help:
	@echo "This makefile for repo-level activity"



PRODUCT_PORT ?= 8001
ORDER_PORT ?= 8002
HOST ?= 127.0.0.1

VENV_PYTHON = ../.venv/bin/python

.PHONY: run-all stop-all

run-all:
	@echo "Запуск микросервисов через venv..."
	cd product_service && $(VENV_PYTHON) -m uvicorn src.app.main:app --host $(HOST) --port $(PRODUCT_PORT) & \
	cd order_service && PRODUCT_SERVICE_URL="http://$(HOST):$(PRODUCT_PORT)" \
	$(VENV_PYTHON) -m uvicorn src.app.main:app --host $(HOST) --port $(ORDER_PORT)

stop-all:
	@echo "Остановка сервисов..."
	@lsof -t -i:$(PRODUCT_PORT) | xargs kill -9 2>/dev/null || true
	@lsof -t -i:$(ORDER_PORT) | xargs kill -9 2>/dev/null || true


