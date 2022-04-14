#!/usr/bin/env sh
env $(cat .env) poetry run pytest -s -vv
