# coding=utf-8

import unittest

from sqlalchemy.orm import sessionmaker

import config
from app import app
from models import Base
from db.sa import build_engine


test_db = config.DB['db']
if '_test' not in test_db:  # 单元测试环境只有一个数据库，测试和 web 都在 diana_test 中
    test_db = '{}_test'.format(test_db)


class BaseTest(unittest.TestCase):
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

        app.testing = True
        cls.app = app
        cls.client = app.test_client()

    def login(self, username, password):
        return self.client.post(
            '/login',
            data=dict(
                username=username,
                password=password
            ),
            follow_redirects=True
        )
