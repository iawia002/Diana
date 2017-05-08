#!/usr/bin/env python
# coding=utf-8

from apps.blog import (
    auth,
    blog,
    statistics,
    tags,
    user,
)


urls = [
    (r'/', blog.Index),  # 首页
    (r'/login', auth.Login),  # 登录页面
    (r'/logout', auth.Logout),  # 登出页面
    (r'/p/(\d+)', blog.Article),
    (r'/p/(\d+)/edit', blog.Edit),
    (r'/tag/(.*)', tags.Tag),
    (r'/tags', tags.Tags),
    (r'/more', blog.More),
    (r'/user', user.User),
    (r'/statistics', statistics.Statistics),
]
