.PHONY: test dev docker-build docker-compose-up docker-compose-down

VERSION := {{cookiecutter.app_version}}
IMAGE_NAME := {{cookiecutter.docker_image_name}}:$(VERSION)

# Detect docker compose command (v2 'docker compose' or v1 'docker-compose')
DOCKER_COMPOSE := $(shell docker compose version > /dev/null 2>&1 && echo "docker compose" || echo "docker-compose")

test:
	@docker run -itd --rm \
		--name mongodb \
		-p 27017:27017 \
		-v $(shell pwd)/data:/data/db \
		mongo:4.4; \
	trap 'docker stop mongodb; docker run --rm -v $(shell pwd)/data:/data alpine sh -c "rm -rf /data/*" || true' EXIT; \
	env $(shell cat .env) poetry run pytest -s -vv

dev:
	@docker run -itd --rm \
		--name mongodb \
		-p 27017:27017 \
		-v $(shell pwd)/data:/data/db \
		mongo:4.4
	@env $(shell cat .env) poetry run gunicorn -k uvicorn.workers.UvicornWorker --reload --bind 0.0.0.0:8888 -w 1 app.server:app

docker-build:
	@docker build -t $(IMAGE_NAME) .

docker-compose-up:
	@$(DOCKER_COMPOSE) up -d --build --remove-orphans --force-recreate

docker-compose-down:
	@$(DOCKER_COMPOSE) down -v --remove-orphans --rmi all
