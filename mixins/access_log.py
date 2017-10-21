#!/usr/bin/env python
# coding=utf-8

from flask import request

from main import db
from utils import ip_region

from models.statistics import AccessLog


def generate_access_log():
    remote_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    data = {
        'remote_ip': remote_ip,
        'uri': request.path,
        'user_agent': request.headers.get('User-Agent'),
        'method': request.method,
        'address': ip_region.memorySearch(remote_ip)['region'].decode('utf-8'),
    }
    db.session.add(AccessLog(**data))
    db.session.commit()
