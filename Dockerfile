FROM python:3.12.4

COPY requirements.txt /tmp/

RUN set -ex \
    && pip --no-cache-dir install -U pip \
    && pip --no-cache-dir install -r /tmp/requirements.txt \
    && rm -f /tmp/requirements.txt

RUN set -ex \
    && mkdir -p /app \
    && touch /app/.keep
WORKDIR /app
