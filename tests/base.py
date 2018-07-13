# coding=utf-8

import unittest

from sqlalchemy.orm import sessionmaker

import config
from app import app
from main import db
from db.sa import build_engine


test_db = config.DB['db']


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
        db.Model.metadata.drop_all(test_engine)
        db.Model.metadata.create_all(test_engine)
        Session = sessionmaker(bind=test_engine)
        cls.Session = Session

        app.testing = True
        cls.app = app
        cls.client = app.test_client()

    def login(self, username, password):
        return self.client.post(
            '/auth/login',
            json={
                'username': username,
                'password': password,
            },
            follow_redirects=True
        )

    def logout(self):
        return self.client.get('/auth/logout', follow_redirects=True)
