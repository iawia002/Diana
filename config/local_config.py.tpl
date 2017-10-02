# coding=utf-8

import os


PSQL_HOST = 'postgres'
SA_URL = 'postgresql+psycopg2://postgres:@postgres/diana'
DB = {
    'user': 'postgres',
    'password': '',
    'host': 'postgres',
    'db': 'diana_test' if os.environ.get('TESTING') else 'diana',
}

ZH_COOKIE = ''
DSN = ''
