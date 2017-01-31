# coding=utf-8

import json
from datetime import date, datetime


class CJsonEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


def error(msg='', **kwargs):
    """ msg: 反馈给用户的信息
    kwargs: 会直接作为Json数据返回
    """
    ret = {
        'status': 'error',
        'msg': msg,
    }
    ret.update(kwargs)
    return json.dumps(ret, indent=2, cls=CJsonEncoder)


def success(msg='', **kwargs):
    """ msg: 反馈给用户的信息
    kwargs: 会直接作为Json数据返回
    """
    ret = {
        'status': 'success',
        'msg': msg,
    }
    ret.update(kwargs)
    return json.dumps(ret, indent=2, cls=CJsonEncoder)
