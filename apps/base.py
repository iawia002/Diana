#!/usr/bin/env python
# coding=utf-8

import tornado.web
from raven.contrib.tornado import SentryMixin

import utils.common
from mixins import AccessLogMixin


class BaseHandler(SentryMixin, tornado.web.RequestHandler, AccessLogMixin):

    def on_finish(self):
        self.generate_access_log()

    def write_error(self, status_code, **kwargs):
        return utils.common.raise_error(request=self, status_code=status_code)


class Redirect(tornado.web.RequestHandler):
    def get(self, path):
        return self.redirect('/' + path)


class NotFound(SentryMixin, tornado.web.RequestHandler, AccessLogMixin):
    def on_finish(self):
        self.generate_access_log()

    def get(self):
        return utils.common.raise_error(request=self, status_code=404)
