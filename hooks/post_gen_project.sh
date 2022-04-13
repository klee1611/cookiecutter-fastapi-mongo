#!/usr/bin/env bash

cd {{cookiecutter.project_dir_name}}
poetry install
mv env.sample .env
