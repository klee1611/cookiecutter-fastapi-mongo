from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi
import yaml
import os
import logging
import logging.config

from .api import health
from .api.v1 import sample_resource as sample_resource_v1

from .db.db import connect_and_init_db, close_db_connect
from .error import BadRequest, UnprocessableError
from .conf.config import Config


# Logging
def replace_env_for_config(log_conf: dict) -> None:
    for k, v in log_conf.items():
        if isinstance(v, dict):
            replace_env_for_config(v)
        elif isinstance(v, str) and v[0] == '$':
            log_conf[k] = os.environ.get(v[1:])


def create_log_config(log_path: str) -> dict:
    with open(log_path, 'r') as f:
        log_config = yaml.load(f, Loader=yaml.CLoader)
        replace_env_for_config(log_config)
    return log_config


log_config = create_log_config('app/conf/logging.yaml')
logging.config.dictConfig(log_config)

# app
app = FastAPI()

app.add_event_handler("startup", Config.app_settings_validate)
app.add_event_handler("startup", connect_and_init_db)
app.add_event_handler("shutdown", close_db_connect)


# openapi schema
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=Config.title,
        version=Config.version,
        routes=app.routes
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


# HTTP error responses
@app.exception_handler(BadRequest)
async def bad_request_handler(req: Request, exc: BadRequest) -> JSONResponse:
    return exc.gen_err_resp()


@app.exception_handler(RequestValidationError)
async def invalid_req_handler(
    req: Request,
    exc: RequestValidationError
) -> JSONResponse:
    logging.error(f'Request invalid. {str(exc)}')
    return JSONResponse(
        status_code=400,
        content={
            "type": "about:blank",
            'title': 'Bad Request',
            'status': 400,
            'detail': [str(exc)]
        }
    )


@app.exception_handler(UnprocessableError)
async def unprocessable_error_handler(
    req: Request,
    exc: UnprocessableError
) -> JSONResponse:
    return exc.gen_err_resp()


# API Path
app.include_router(
    health.router,
    prefix='/health',
    tags=["health"]
)
app.include_router(
    sample_resource_v1.router,
    prefix='/api/sample-resource-app/v1/sample-resource',
    tags=["sample resource v1"]
)
