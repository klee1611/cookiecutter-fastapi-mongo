#!/usr/bin/env bash
cd ..
cookiecutter cookiecutter-fastapi-mongo --no-input
cd demo-project
env $(cat .env) poetry run pytest -s -vv
poetry env remove python
cd ..
rm -rf demo-project
