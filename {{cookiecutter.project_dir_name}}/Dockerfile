FROM python:3.10.0-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN adduser --disabled-password --gecos '' appuser
WORKDIR /server

# Install curl and uv
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl ca-certificates && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    apt-get remove -y curl && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml uv.lock ./
RUN uv export --no-hashes --no-dev -o requirements.txt && \
        sed -i '/^-e \./d' requirements.txt && \
        chown appuser:appuser requirements.txt && \
        pip install --no-cache-dir -r requirements.txt

USER appuser
COPY --chown=appuser:appuser start.sh /server/
COPY --chown=appuser:appuser app /server/app

RUN chmod +x /server/start.sh
ENTRYPOINT [ "/server/start.sh" ]
