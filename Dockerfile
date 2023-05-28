FROM python:3.10.5-alpine

ENV POETRY_VERSION=1.4.2

WORKDIR /opt/src/

RUN apk update
RUN pip install --upgrade pip

COPY poetry.lock pyproject.toml ./

RUN apk add --no-cache gcc build-base libffi-dev musl-dev

RUN yes | pip install --no-cache-dir "poetry==$POETRY_VERSION" \
    && poetry config virtualenvs.create false  \
    && poetry install --only main --no-interaction --no-ansi --no-cache

COPY ./src .
