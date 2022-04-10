#!/usr/bin/env bash
cd ..
cookiecutter cookiecutter-fastapi-mongo --no-input
cd demo-project
pipenv run pytest -s -vv
pipenv --rm
cd ..
rm -rf demo-project
