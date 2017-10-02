# coding=utf-8

import logging
import datetime

from flask import Flask
from raven.contrib.flask import Sentry

import config
from celery_ser import make_celery
from mixins.access_log import generate_access_log

from apps.blog.urls import bp as blog
from apps.fish.urls import bp as fish


app = Flask(__name__, template_folder='static/dist')
app.config.update(
    DEBUG=config.DEBUG,
    SECRET_KEY=config.SECRET_KEY,
    SESSION_COOKIE_NAME='diana',
    PERMANENT_SESSION_LIFETIME=datetime.timedelta(days=365),
    SESSION_REFRESH_EACH_REQUEST=False,
)
sentry = Sentry()
sentry.init_app(
    app,
    dsn=config.DSN,
    logging=True,
    level=logging.ERROR,
)
celery = make_celery(app)


@app.after_request
def access_log(response):
    generate_access_log()
    return response


# url
app.register_blueprint(blog)
app.register_blueprint(fish)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8004)
