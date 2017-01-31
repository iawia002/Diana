#!/usr/bin/env python
# coding=utf-8

try:
    import urlparse  # py2  # noqa
except ImportError:
    import urllib.parse as urlparse  # py3  # noqa


def login_require(func):
    def wrapper(*args, **kwargs):
        self = args[0]
        user_id = self.get_secure_cookie('diana')
        if user_id:
            self.user_id = user_id
            return func(*args, **kwargs)
        else:
            return self.redirect('/')

    return wrapper


# def next():
#     if "?" not in url:
#         if urlparse.urlsplit(url).scheme:
#             # if login url is absolute, make next absolute too
#             next_url = self.request.full_url()
#         else:
#             next_url = self.request.uri
#         url += "?" + urlencode(dict(next=next_url))
#     self.redirect(url)
