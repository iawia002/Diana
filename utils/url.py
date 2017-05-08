#!/usr/bin/env python
# coding=utf-8

from __future__ import unicode_literals

from importlib import import_module


def include(module):
    '''
    引入 urls.py 中的 urls list
    module: apps.hello.urls
    urls: apps.hello.urls.urls
    '''
    res = import_module(module)
    urls = getattr(res, 'urls', res)
    return urls


def url_wrapper(urls):
    '''
    将子应用中的 urls 列表中的每一项的路径和其主路径拼接起来

    urls
    [
        (u'/', [
            ('', <class 'apps.hello.views.Index'>),
            ('2', <class 'apps.hello.views.Index2'>)
        ])
    ]
    '''
    wrapper_list = []
    for url in urls:
        path, handles = url
        if isinstance(handles, (tuple, list)):
            for handle in handles:
                pattern, handle_class = handle
                wrap = ('{0}{1}'.format(path, pattern), handle_class)
                wrapper_list.append(wrap)
        else:
            wrapper_list.append((path, handles))
    return wrapper_list
