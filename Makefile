APP_NAME=fastapi_app
COMPOSE_FILE=docker-compose.yml

.PHONY: build
build:
	docker-compose -f $(COMPOSE_FILE) build

.PHONY: up
up:
	docker-compose -f $(COMPOSE_FILE) up -d

.PHONY: stop
stop:
	docker-compose -f $(COMPOSE_FILE) stop

.PHONY: down
down:
	docker-compose -f $(COMPOSE_FILE) down

.PHONY: logs
logs:
	docker-compose -f $(COMPOSE_FILE) logs -f

.PHONY: test
test:
	docker-compose -f $(COMPOSE_FILE) run --rm app pytest