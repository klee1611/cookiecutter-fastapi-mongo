#!/usr/bin/env bash

docker-compose stop && \
    docker-compose rm -f && \
    docker-compose build --no-cache && \
    docker-compose up -d
