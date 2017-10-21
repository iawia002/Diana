# coding=utf-8

import config as app_config
import multiprocessing


bind = '{host}:{port}'.format(
    host=app_config.HOST, port=app_config.PORT
)
workers = multiprocessing.cpu_count() * 2
worker_class = 'gevent'

access_log_format = (
    '%(t)s %({X-Real-IP}i)s %(u)s "%(r)s" '
    '%(s)s %(b)s "%(f)s" "%(a)s" %(T)s %(D)s'
)

if app_config.DEBUG:
    accesslog = '-'
    errorlog = '-'
    reload = True
else:
    accesslog = 'log/diana_web_access.log'
    errorlog = 'log/diana_web_error.log'
