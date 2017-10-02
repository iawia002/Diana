#!/usr/bin/env python
# coding=utf-8

import random

from flask import (
    render_template,
)

import config


def raise_error(status_code):
    data = {}
    data['bg'] = random.choice(config.INDEX_BG)
    data['status'] = {}
    data['status']['code'] = status_code
    return render_template('blog/error.html', data=data), status_code


def row2dict(row):
    data = {}
    for column in row.__table__.columns:
        data[column.name] = getattr(row, column.name)

    return data
