# Backend FastAPI and MongoDB - Project Template
![Python3.10](https://img.shields.io/badge/Python-3.10-brightgreen.svg?style=flat-square)
![MongoDB](https://img.shields.io/badge/MongoDB-3.6-brightgreen.svg?style=flat-square)
![Lint](https://github.com/klee1611/cookiecutter-fastapi-mongo/actions/workflows/lint.yml/badge.svg)
![CI Tests](https://github.com/klee1611/cookiecutter-fastapi-mongo/actions/workflows/ci.yml/badge.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)


This is a backend boilerplate designed for high-performance RESTful APIs using FastAPI and Motor, an asynchronous driver for MongoDB. It includes a health API for service health checking, basic CRUD operations for a sample resource, Swagger API documentation, and Docker support. Additionally, this boilerplate uses Cookiecutter, allowing for easy creation of new backend services.

![api document screenshot](screenshot/api_document.png)

## Features
A new backend project created with this boilerplate provides:
- [x] Asynchronous high-performance RESTful APIs built upon [FastAPI](https://fastapi.tiangolo.com/) framework.
- [x] Asynchronous CRUD operations for a sample resource built upon [Motor](https://motor.readthedocs.io/en/stable/) driver for MongoDB, providing high performance and efficiency.
- [x] API documentation with [Swagger UI](https://swagger.io/tools/swagger-ui/).
- [x] API testing with [pytest](https://docs.pytest.org/en/7.1.x/) and [pytest-asyncio](https://github.com/pytest-dev/pytest-asyncio).
- [x] Dockerfile for containerization and docker-compose support.
- [x] Easy creation of new backend services with [cookiecutter](https://github.com/cookiecutter/cookiecutter).
- [x] Easy package menagement with [Poetry](https://python-poetry.org/).
- [x] Health API for service health checking.
- [x] Easy configuration with environment variables.
- [x] Easy testing, develop running, docker build, docker-compose up and down with Makefile.
- [x] Proper logging with ID masking.

## Prerequisites
- Python 3.10+
- [Poetry 2.2.1](https://python-poetry.org/) installed
- [Cookiecutter](https://github.com/cookiecutter/cookiecutter) installed
- Docker installed
- GNU Make

## Getting Started

### ⚠️ IMPORTANT: Create A New Service First
**You must execute this command before any other usage.**  
With [Cookiecutter](https://github.com/cookiecutter/cookiecutter), you don't have to fork this project to create a new service.

Go to the directory where you want to place your new backend project, and run:

```sh
cookiecutter gh:klee1611/cookiecutter-fastapi-mongo
```

After the project folder is created, all packages required will be installed automatically.  
**All subsequent steps below should be run inside the newly created project directory.**  

### Edit Environment Variables
Edit the `.env` file within the project folder.

### Run Tests
```sh
make test
```

### Build Docker Image
```sh
make docker-build
```

### Docker-compose
```sh
make docker-compose-up
make docker-compose-down
```

### Run Service Locally
```sh
make dev
```
This will create a MongoDB container as well.

### Check Swagger API Document
Go to ` http://localhost:8888/docs`.

## Website Deployment

The project website is located in the `website/` directory.

**Primary Method (Automatic):**  
The website is automatically deployed to GitHub Pages via GitHub Actions when changes are pushed to `main` or `develop` branches. See `.github/workflows/deploy-pages.yml` for the workflow configuration.

**Manual Deployment (Optional):**  
For manual deployments or testing, you can use the npm gh-pages package:

```sh
cd website
npm install
npm run deploy
```

Note: Manual deployment should only be used for testing or emergency updates. The GitHub Actions workflow is the authoritative deployment method.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you.
