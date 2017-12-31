# coding=utf-8

from importlib import import_module

import config
import utils.common
from main import app
from mixins.access_log import generate_access_log


@app.after_request
def access_log(response):
    generate_access_log()
    return response


app.url_map.strict_slashes = False

# url
apps = ['blog', 'auth', 'fish']
for _app in apps:
    try:
        url = import_module('apps.{}.urls'.format(_app))
    except Exception:
        continue
    app.register_blueprint(url.bp)


# error
app.register_error_handler(
    404, lambda e: utils.common.raise_error(status_code=404)
)
app.register_error_handler(
    500, lambda e: utils.common.raise_error(status_code=500)
)


if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT)
