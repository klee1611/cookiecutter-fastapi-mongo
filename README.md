# Backend FastAPI and MongoDB - Project Template
![Lint](https://github.com/klee1611/cookiecutter-fastapi-mongo/actions/workflows/lint.yml/badge.svg)
![CI Tests](https://github.com/klee1611/cookiecutter-fastapi-mongo/actions/workflows/ci.yml/badge.svg)

A template to a high performance backend project using Python, FastAPI, and MongoDB,  
with the API documentation.  
The purpose of this template is to build a small, independent backend service for microservices architecture.  

![api document screenshot](screenshot/api_document.png)

# Features
A project created by this template provides a high performance RESTful API for a sample resource,  
with:
* Basic CRUD operation with updating time record
* API documentation with [Swagger UI](https://swagger.io/tools/swagger-ui/)
* API testing
* Proper logging with ID masking
* Dockerfile and docker-compose support

## Build Upon
* [FastAPI](https://fastapi.tiangolo.com/) for asynchronous backend framework and API documentation.
* [Motor](https://motor.readthedocs.io/en/stable/) for asynchronous MongoDB operations.
* [pytest](https://docs.pytest.org/en/7.1.x/) and [pytest-asyncio](https://github.com/pytest-dev/pytest-asyncio) for API testing.
* [Poetry](https://python-poetry.org/) for package management.

# Quick Start
To use this template,  
you don't have to fork this project,  
just use [cookiecutter](https://github.com/cookiecutter/cookiecutter).  

First,  
install cookiecutter if you don't already have it:
```sh
pip3 install cookiecutter
```

and since this template uses `poetry` as the Python package manager,  
install `poetry` before creating a project:
```sh
pip3 install poetry
```
Be careful of the `pip3` version.  
`poetry` should be installed with `pip3` version above Python 3.10.  

Then go to the directory where you want to place your project,  
and create the new project with this template and `cookiecutter`:
```sh
cookiecutter gh:klee1611/cookiecutter-fastapi-mongo
```

After the project folder is created,  
the template will install all the packages required for development automatically.  

# Troubleshooting
### Testing Failed with Wrong `pytest` Version
Check the `pytest` version from the testing output.  
If the `pytest` version is lower than `Python3.10`,  
it might be caused by the `poetry` issue.  

Using `pip3` installed with Python3.10 or above to install `pip3` will solve this issue most likely.  
