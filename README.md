<a href="https://github.com/apirobot/django-channels-celery-jokes">
    <p align="center">
      <img src="https://raw.githubusercontent.com/apirobot/django-channels-celery-jokes/master/preview.gif" alt="django-channels-celery-jokes">
    </p>
</a>

---

## Description

It's a simple web app that makes requests in the background to the API with random jokes using [celery](https://github.com/celery/celery) library and then sends these jokes through the WebSockets to the users using [channels](https://github.com/django/channels) library.

## How to run

Just clone the repo, go into the directory and then run:

```bash
$ docker-compose up
```

That's all. Isn't Docker amazing?
