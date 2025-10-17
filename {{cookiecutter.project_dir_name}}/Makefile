.PHONY: test dev docker-build docker-compose-up docker-compose-down

VERSION := {{cookiecutter.app_version}}
IMAGE_NAME := {{cookiecutter.docker_image_name}}:$(VERSION)

test:
	@docker run -itd --rm \
		--name mongodb \
		-p 27017:27017 \
		-v $(shell pwd)/data:/data/db \
		mongo:3.6
	@env $(shell cat .env) poetry run pytest -s -vv
	@docker stop mongodb

dev:
	@docker run -itd --rm \
		--name mongodb \
		-p 27017:27017 \
		-v $(shell pwd)/data:/data/db \
		mongo:3.6
	@env $(shell cat .env) poetry run gunicorn -k uvicorn.workers.UvicornWorker --reload --bind 0.0.0.0:8888 -w 4 app.server:app

docker-build:
	@docker build -t $(IMAGE_NAME) .

docker-compose-up:
	@docker compose up -d --build --remove-orphans --force-recreate || docker-compose up -d --build --remove-orphans --force-recreate

docker-compose-down:
	@docker compose down -v --remove-orphans --rmi all || docker-compose down -v --remove-orphans --rmi all
