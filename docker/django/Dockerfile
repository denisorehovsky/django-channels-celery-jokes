FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev

WORKDIR /app
COPY . /app

RUN pip install pipenv \
  && pipenv install --deploy --system --ignore-pipfile

COPY ./docker/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

COPY ./docker/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r//' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./docker/django/celery/beat/start /start-celerybeat
RUN sed -i 's/\r//' /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./docker/django/channels/server/start /start-channelsserver
RUN sed -i 's/\r//' /start-channelsserver
RUN chmod +x /start-channelsserver
