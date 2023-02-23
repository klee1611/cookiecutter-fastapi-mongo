FROM python:3.10.0-slim-bullseye

WORKDIR /server

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install poetry
COPY pyproject.toml poetry.lock /tmp
RUN cd /tmp && \
        poetry export --without-hashes --without dev -f requirements.txt -o requirements.txt && \
        pip install -r requirements.txt

COPY start.sh /server/
COPY app /server/app

RUN chmod +x /server/start.sh
ENTRYPOINT [ "/server/start.sh" ]
