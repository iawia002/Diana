#!/usr/bin/env python
# coding=utf-8

from flask import request

import utils.db
from main import db
from utils import ip_region

from models.statistics import AccessLog


def generate_access_log():
    data = {
        'remote_ip': request.remote_addr,
        'uri': request.path,
        'user_agent': request.headers.get('User-Agent'),
        'method': request.method,
        'address': ip_region.memorySearch(
            request.remote_addr
        )['region'].decode('utf-8'),
    }
    access_log = utils.db.get_instance(db.session, AccessLog, **data)
    if not access_log.views:
        access_log.views = 0
    access_log.views += 1
    db.session.add(access_log)
    db.session.commit()
