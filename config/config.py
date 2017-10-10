#!/usr/bin/env python
# coding=utf-8

import os
import datetime

DEBUG = False
HOST = '0.0.0.0'
PORT = 8004

# redis
REDIS_HOST = 'redis'
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_DB = 0
REDIS_HOST_PORT = '%(host)s:%(port)s' % {
    'host': REDIS_HOST,
    'port': REDIS_PORT
}

# PSQL
PSQL_HOST = 'localhost'

# sqlalchemy
# Alembic 要用这个 url
SA_URL = 'postgresql+psycopg2://:@/diana'
DB = {
    'user': 'postgres',
    'password': '',
    'host': 'postgres',
    'db': 'diana_test' if os.environ.get('TESTING') else 'diana',
}

# Time
TIME_NOW = datetime.datetime.now()
TIME_TOMORROW = datetime.date.today() + datetime.timedelta(days=2)

ARTICLE_PAGE_NUMBER = 10
SECRET_KEY = 'sfljKLYIOY9&()()*))ljsfl&^%*'
USER_ID = 1

ZH_COOKIE = ''

# Sentry
DSN = ''


try:
    from .local_config import *  # noqa
except ImportError:
    pass
