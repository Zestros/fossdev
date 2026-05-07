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

# 🐳 🐳 🐳 🐳 🐳 ДОКЕРЫ!!!

NETWORK = services-net
COMPOSE_FILE = docker-compose.yaml

# DOCKER RUN

.PHONY: run-docker stop-docker


run-docker:
	@echo "Создание сети..."
	docker network create $(NETWORK) || true

	@echo "Запуск инфраструктуры..."

	docker run -d --name db \
	--network $(NETWORK) \
	-e POSTGRES_USER=app \
	-e POSTGRES_PASSWORD=app \
	-e POSTGRES_DB=orders \
	-p 5432:5432 \
	postgres:16

	docker run -d --name redis \
	--network $(NETWORK) \
	-p 6379:6379 \
	redis:7

	@echo "Запуск product-service..."
	docker run -d --name product-service \
	--network $(NETWORK) \
	-p 8001:8000 \
	product-service

	@echo "Запуск discount-service..."
	docker run -d --name discount-service \
	--network $(NETWORK) \
	-p 8003:8000 \
	-e REDIS_URL=redis://redis:6379 \
	discount-service

	@echo "Запуск order-service..."
	docker run -d --name order-service \
	--network $(NETWORK) \
	-p 8002:8000 \
	-e PRODUCT_SERVICE_URL=http://product-service:8000 \
	-e DISCOUNT_SERVICE_URL=http://discount-service:8000 \
	-e DATABASE_URL=postgresql://app:app@db:5432/orders \
	order-service

stop-docker:
	@echo "Остановка контейнеров..."
	docker rm -f product-service discount-service order-service db redis 2>/dev/null || true
	docker network rm $(NETWORK) 2>/dev/null || true


# DOCKER COMPOSE

.PHONY: run-compose stop-compose rebuild

run-compose:
	@echo "Запуск через Docker Compose..."
	docker compose -f $(COMPOSE_FILE) up --build

stop-compose:
	@echo "Остановка compose..."
	docker compose -f $(COMPOSE_FILE) down

rebuild:
	@echo "Пересборка без кеша..."
	docker compose -f $(COMPOSE_FILE) build --no-cache

.PHONY: clean

clean:
	@echo "Очистка Docker системы..."
	docker system prune -f

