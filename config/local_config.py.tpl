# coding=utf-8

import os


DB = {
    'user': 'postgres',
    'password': '',
    'host': 'postgres',
    'db': 'diana_test' if os.environ.get('TESTING') else 'diana',
}

ZH_COOKIE = ''
DSN = ''
