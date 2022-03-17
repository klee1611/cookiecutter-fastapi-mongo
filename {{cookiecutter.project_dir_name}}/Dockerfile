FROM python:3.10.0-slim-bullseye

WORKDIR /server

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile* /tmp
RUN cd /tmp && pipenv lock --keep-outdated --requirements > /server/requirements.txt
RUN cd /server && pip install -r requirements.txt

COPY start.sh /server/
COPY app /server/app

RUN chmod +x /server/start.sh
ENTRYPOINT [ "/server/start.sh" ]
