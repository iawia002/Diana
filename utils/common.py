#!/usr/bin/env python
# coding=utf-8

from flask import (
    jsonify,
)


def raise_error(status_code):
    data = {
        'error': status_code
    }
    return jsonify(data), status_code


def row2dict(row):
    data = {}
    for column in row.__table__.columns:
        data[column.name] = getattr(row, column.name)

    return data
