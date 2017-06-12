#!/usr/bin/env python
# coding=utf-8

from sqlalchemy.orm import sessionmaker
from tornado.testing import AsyncHTTPTestCase

import config
from models import Base
from app import application
from db.sa import build_engine


application.settings['xsrf_cookies'] = False
test_db = config.DB['db']
if '_test' not in test_db:  # 单元测试环境只有一个数据库，测试和 web 都在 diana_test 中
    test_db = '{}_test'.format(test_db)


class BaseTest(AsyncHTTPTestCase):
    def get_app(self):
        return application

    @classmethod
    def setUpClass(cls):
        engine = build_engine(db='postgres')
        conn = engine.connect()
        # conn.autocommit = True
        try:
            conn.execute('commit')
            conn.execute('drop database {}'.format(test_db))
        except Exception:
            pass
        conn.execute('commit')
        conn.execute('create database {}'.format(test_db))
        conn.close()
        test_engine = build_engine(db=test_db)
        Base.metadata.drop_all(test_engine)
        Base.metadata.create_all(test_engine)
        Session = sessionmaker(bind=test_engine)
        cls.Session = Session
