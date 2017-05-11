#!/usr/bin/env python
# coding=utf-8

from apps.fish import views


urls = [
    (r'', views.Index),  # 首页
    (r'/p/(\d+)', views.Article),
    (r'/more', views.More),
]
