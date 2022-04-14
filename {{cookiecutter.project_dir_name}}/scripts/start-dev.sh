#!/usr/bin/env sh
env $(cat .env) poetry run gunicorn -k uvicorn.workers.UvicornWorker --reload --bind 0.0.0.0:8888 -w 4 app.server:app
