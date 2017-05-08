#!/usr/bin/env python
# coding=utf-8

import utils.db
from utils import ip_region

from db.sa import Session
from models.statistics import AccessLog


class AccessLogMixin(object):

    def generate_access_log(self):
        request = self.request
        data = {
            'remote_ip': request.remote_ip,
            'uri': request.uri,
            'module': self.__class__.__name__,
            'user_agent': request.headers['User-Agent'],
            'method': request.method,
            'address': ip_region.memorySearch(
                request.remote_ip
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
