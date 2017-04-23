#!/usr/bin/env python
# coding=utf-8

import tornado.web

import utils.common
from mixins import AccessLogMixin


class BaseHandler(tornado.web.RequestHandler, AccessLogMixin):

    def prepare(self):
        self.generate_access_log()

    def write_error(self, status_code, **kwargs):
        return utils.common.raise_error(request=self, status_code=status_code)
