# coding=utf-8

from celery import (
    Celery,
    # platforms,
)
from raven import Client
from raven.contrib.celery import register_signal, register_logger_signal

from config import (
    config,
    celery_config,
)


class CeleryWithSentry(Celery):

    def on_configure(self):
        client = Client(config.DSN)
        # register a custom filter to filter out duplicate logs
        register_logger_signal(client)
        # hook into the Celery error handler
        register_signal(client)


def make_celery(app):
    celery = CeleryWithSentry(app.import_name)
    celery.config_from_object(celery_config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery


# platforms.C_FORCE_ROOT = True
