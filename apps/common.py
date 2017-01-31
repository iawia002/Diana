#!/usr/bin/env python
# coding=utf-8

import tornado.web

import utils.common


class Redirect(tornado.web.RequestHandler):
    def get(self, path):
        return self.redirect('/' + path)


class NotFound(tornado.web.RequestHandler):
    def get(self):
        return utils.common.raise_error(request=self, status_code=404)
