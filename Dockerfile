FROM python:3.8-alpine

ENV PYTHONUNBUFFERED=true

RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev

RUN mkdir -p /app
WORKDIR /app

COPY ./src /app/

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt


