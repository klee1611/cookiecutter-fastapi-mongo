#!/usr/bin/env bash

cd {{cookiecutter.project_dir_name}}
pipenv install --dev
mv env.sample .env
