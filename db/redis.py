#!/usr/bin/env python
# coding=utf-8

import redis
from config import config


def get_redis():
    return redis.Redis(
        host=config.REDIS_HOST,
        port=config.REDIS_PORT,
        db=config.REDIS_DB,
        socket_timeout=10,
    )


def get_redis_pool():
    redis_pool = redis.ConnectionPool(
        host=config.REDIS_HOST,
        port=config.REDIS_PORT
    )
    return redis.Redis(connection_pool=redis_pool, db=config.REDIS_DB)
