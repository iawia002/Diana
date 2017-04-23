#!/usr/bin/env python
# coding=utf-8

from db.sa import Session
from utils.common import row2dict
from utils.auth import login_require
from apps.model import AccessLog as AccessLogModel

from apps.base import BaseHandler


class AccessLog(BaseHandler):

    @login_require
    def get(self):
        session = Session()
        log_instance = session.query(AccessLogModel).all()
        logs = []
        for log in log_instance:
            logs.append(row2dict(log))
        return self.write({'data': logs})
