# coding=utf-8

# import logging

import config

from mixins.access_log import generate_access_log

from main import app
from apps.blog.urls import bp as blog
from apps.fish.urls import bp as fish


# logger = logging.getLogger('werkzeug')
# logger.addHandler(logging.StreamHandler())


@app.after_request
def access_log(response):
    generate_access_log()

    # if response.status_code != 500:
    #     logger.error('{} {} {} {} {} {}'.format(
    #         datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    #         request.remote_addr,
    #         request.method,
    #         request.scheme,
    #         request.full_path,
    #         response.status
    #     ))
    return response


# url
app.register_blueprint(blog)
app.register_blueprint(fish)


if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT)
