# coding=utf-8

import logging
import datetime

from flask import Flask
from raven.contrib.flask import Sentry
from flask_sqlalchemy import SQLAlchemy

import config
from db.sa import build_sa_url
from celery_ser import make_celery


app = Flask(__name__, template_folder='static/dist')
app.config.update(
    DEBUG=config.DEBUG,
    SECRET_KEY=config.SECRET_KEY,
    SESSION_COOKIE_NAME='diana',
    PERMANENT_SESSION_LIFETIME=datetime.timedelta(days=365),
    SESSION_REFRESH_EACH_REQUEST=False,
    SQLALCHEMY_DATABASE_URI=build_sa_url(
        user=config.DB['user'],
        password=config.DB['password'],
        host=config.DB['host'],
        db=config.DB['db'],
    ),
    SQLALCHEMY_POOL_SIZE=200,
    SQLALCHEMY_MAX_OVERFLOW=10,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
sentry = Sentry()
sentry.init_app(
    app,
    dsn=config.DSN,
    logging=True,
    level=logging.ERROR,
)
celery = make_celery(app)
db = SQLAlchemy(app)
