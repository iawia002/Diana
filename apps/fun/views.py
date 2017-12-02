# coding=utf-8

from flask import (
    render_template,
)
from flask.views import MethodView


class Index(MethodView):
    '''
    首页
    '''
    def get(self):
        return render_template('fun/index.html')
