#!/usr/bin/env python
# coding=utf-8

import random

import config


def raise_error(request, status_code):
    data = {}
    data['bg'] = random.choice(config.INDEX_BG)
    data['status'] = {}
    data['status']['code'] = status_code
    request.set_status(status_code)
    return request.render('blog/error.html', data=data)


def row2dict(row):
    data = {}
    for column in row.__table__.columns:
        data[column.name] = getattr(row, column.name)

    return data
