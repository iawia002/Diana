#!/usr/bin/env python
# coding=utf-8

from __future__ import absolute_import

import config
from db.sa import Session
from apps.fish.models import Record


def article(page):
    '''
    page 从 1 开始
    '''
    page = int(page)
    session = Session()
    records = session.query(Record).order_by(Record.create_time.desc())[
        (page-1)*config.ARTICLE_PAGE_NUMBER: page*config.ARTICLE_PAGE_NUMBER
    ]
    records = [record.json for record in records]
    session.commit()
    session.close()
    return records
