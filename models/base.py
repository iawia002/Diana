# coding=utf-8

import datetime

from main import db


class CreateTimeMixin:

    create_time = db.Column(
        db.DateTime,
        default=datetime.datetime.now,
    )


class UpdateTimeMixin(CreateTimeMixin):
    update_time = db.Column(
        db.DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
    )
