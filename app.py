# coding=utf-8

import os

import tornado.web
import tornado.ioloop
from tornado.options import (
    define,
    options,
)

import config
import apps.base
from utils.url import (
    include,
    url_wrapper,
)


# 在options中设置几个变量
define('port', default=8004, help='run on this port', type=int)
define('debug', default=False, help='enable debug mode')


class Application(tornado.web.Application):
    def __init__(self):
        handlers = url_wrapper([
            (r'/(.*)/', apps.base.Redirect),  # 保证网址有无'/'结尾，都能指向同一个类。
            (r'', include('apps.blog.urls')),  # 博客
            (r'/fish', include('apps.fish.urls')),  #
        ])
        template_path = os.path.join(
            os.path.dirname(__file__), 'static/dist/'
        )
        settings = {
            'static_path': os.path.join(
                os.path.dirname(__file__), 'static'
            ),
            'template_path': template_path,
            'cookie_secret': config.SECRET_KEY,
            'default_handler_class': apps.base.NotFound,
            'login_url': '/login',
            'xsrf_cookies': True,
            'debug': options.debug,
            'gzip': True,
            'autoescape': None
        }
        super(Application, self).__init__(handlers, **settings)

# 解析命令行
tornado.options.parse_command_line()
application = Application()


def main():
    application.listen(options.port, xheaders=True)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
