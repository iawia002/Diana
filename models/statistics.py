# coding=utf-8

import sqlalchemy as sa

from models import Base


class AccessLog(Base):
    __tablename__ = 'access_log'

    id = sa.Column(
        sa.Integer,
        primary_key=True,
    )
    remote_ip = sa.Column(
        sa.String(15),
    )
    uri = sa.Column(
        sa.String,
    )
    user_agent = sa.Column(
        sa.String,
    )
    method = sa.Column(
        sa.String(7),
    )
    views = sa.Column(
        sa.Integer,
        default=0,
    )
    address = sa.Column(
        sa.String(100),
    )

    def __repr__(self):
        return '<AccessLog(remote_ip={})>'.format(self.remote_ip)
