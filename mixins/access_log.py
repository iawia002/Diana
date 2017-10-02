#!/usr/bin/env python
# coding=utf-8

from flask import request

import utils.db
from utils import ip_region

from db.sa import Session
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
    session = Session()
    access_log = utils.db.get_instance(session, AccessLog, **data)
    if not access_log.views:
        access_log.views = 0
    access_log.views += 1
    session.add(access_log)
    session.commit()
    session.close()
