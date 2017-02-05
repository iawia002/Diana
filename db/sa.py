#!/usr/bin/env python
# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config

engine = create_engine(
    config.SA_URL,
    client_encoding='utf8',
    pool_size=200,
    max_overflow=10,
)

Session = sessionmaker(bind=engine)
session = Session()
