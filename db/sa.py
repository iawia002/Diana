#!/usr/bin/env python
# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config


def build_engine(
    user=config.DB['user'], password=config.DB['password'],
    host=config.DB['host'], db=config.DB['db']
):
    sa_url = 'postgresql+psycopg2://{user}:{password}@{host}/{db}'.format(
        user=user, password=password, host=host, db=db
    )
    return create_engine(
        sa_url,
        client_encoding='utf8',
        pool_size=200,
        max_overflow=10,
    )


Session = sessionmaker(bind=build_engine())
session = Session()
