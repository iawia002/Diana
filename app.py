# coding=utf-8

import os
import logging
import datetime
from concurrent.futures import ThreadPoolExecutor

import tornado.web
import tornado.ioloop
from tornado import gen
from tornado.options import (
    define,
    options,
)

import config
import apps.base
from apps.fish.crawler.zhihu import jike
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

thread_pool = ThreadPoolExecutor(2)


@gen.coroutine
def loop():
    while True:
        logging.info(
            '{}: update start'.format(
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            )
        )
        result = yield thread_pool.submit(jike)
        logging.info('update result: {}'.format(result))
        yield gen.sleep(60 * 60 * 0.5)


def main():
    application.listen(options.port, xheaders=True)
    tornado.ioloop.IOLoop.current().spawn_callback(loop)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
