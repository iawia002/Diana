#!/usr/bin/env python
# coding=utf-8

import tornado.web

import utils.common


class BaseHandler(tornado.web.RequestHandler):
    def write_error(self, status_code, **kwargs):
        return utils.common.raise_error(request=self, status_code=status_code)
