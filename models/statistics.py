# coding=utf-8

from main import db
from models.base import CreateTimeMixin


class AccessLog(CreateTimeMixin, db.Model):
    __tablename__ = 'access_log'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    remote_ip = db.Column(
        db.String(15),
    )
    uri = db.Column(
        db.String,
    )
    user_agent = db.Column(
        db.String,
    )
    referrer = db.Column(
        db.String,
    )
    method = db.Column(
        db.String(7),
    )
    address = db.Column(
        db.String(100),
    )

    def __repr__(self):
        return '<AccessLog(remote_ip={})>'.format(self.remote_ip)
