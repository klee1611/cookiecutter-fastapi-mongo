#!/usr/bin/env sh
if [ -n "$1" ]; then
    if [ $1 = '--dev' ]; then
        echo "Apply dev config"
        export CONFIG_NAME='development'
        gunicorn -k uvicorn.workers.UvicornWorker --reload --bind 0.0.0.0:8888 -w 4 app.server:app
    fi
else
    gunicorn -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8888 -w 4 app.server:app
fi
