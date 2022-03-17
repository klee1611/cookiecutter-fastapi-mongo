#!/usr/bin/env bash

cd {{cookiecutter.project_dir_name}}
pipenv install
mv env.sample .env
