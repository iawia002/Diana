#!/usr/bin/env python
# coding=utf-8

import random

from config import config


def raise_error(request, status_code):
    data = {}
    data['bg'] = random.choice(config.INDEX_BG)
    data['status'] = {}
    data['status']['code'] = status_code
    request.set_status(status_code)
    return request.render('error.html', data=data)
