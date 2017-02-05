#!/usr/bin/env python
# coding=utf-8

import psycopg2
import psycopg2.pool
import psycopg2.extras

from DBUtils.PooledDB import PooledDB

import config


class psql(object):

    def connect(self):
        self.conn = psycopg2.connect(
            dbname='diana',
            host=config.PSQL_HOST,
            user='postgres'
        )
        self.cursor = self.conn.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor
        )

    def close(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()


class psql_pool(object):
    __pool = None

    def __init__(self):
        self.conn = None

    @staticmethod
    def __get_conn():
        if psql_pool.__pool is None:
            __pool = psycopg2.pool.SimpleConnectionPool(
                minconn=1,
                maxconn=100,
                database='diana',
                host=config.PSQL_HOST,
                user='postgres'
            )
        return __pool.getconn()

    def connect(self):
        self.conn = psql_pool.__get_conn()
        self.cursor = self.conn.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor
        )

    def close(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()
        # __pool.putconn(self.conn)


class pool(object):
    __pool = None

    @staticmethod
    def __get_conn():
        if pool.__pool is None:
            __pool = PooledDB(
                creator=psycopg2,
                mincached=1,
                maxcached=100,
                database='diana',
                host=config.PSQL_HOST,
                user='postgres'
            )
        return __pool.connection()

    def connect(self):
        self.conn = pool.__get_conn()
        self.cursor = self.conn.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor
        )

    def close(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()
