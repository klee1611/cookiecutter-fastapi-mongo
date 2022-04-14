#!/usr/bin/env bash
cd ..
cookiecutter cookiecutter-fastapi-mongo --no-input
cd demo-project
./scripts/start-dev.sh
poetry env remove python3
cd ..
rm -rf demo-project
