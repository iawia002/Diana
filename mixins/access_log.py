#!/usr/bin/env python
# coding=utf-8

from flask import request

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
    db.session.add(AccessLog(**data))
    db.session.commit()
