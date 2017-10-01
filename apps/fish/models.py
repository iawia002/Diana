# coding=utf-8

import datetime

import sqlalchemy as sa

from models import Base


class Record(Base):
    '''
    所有钓鱼帖的记录
    '''
    __tablename__ = 'fish_record'

    record_id = sa.Column(
        sa.Integer,
        primary_key=True,
    )
    create_time = sa.Column(
        sa.DateTime,
        default=datetime.datetime.now,
    )
    update_time = sa.Column(
        sa.DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
    )
    title = sa.Column(
        sa.String(100),
    )
    content = sa.Column(
        sa.ARRAY(sa.String),
    )
    image_num = sa.Column(
        sa.Integer,
    )
    source = sa.Column(
        sa.String(1000),
    )
    views = sa.Column(
        sa.Integer,
        default=0,
    )

    def __repr__(self):
        return "<Record(id='%d')>" % self.record_id

    @property
    def json(self):
        return {
            'record_id': self.record_id,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
            'update_time': self.update_time.strftime('%Y-%m-%d %H:%M:%S'),
            'title': self.title,
            'content': self.content,
            'image_num': self.image_num,
            'source': self.source,
            'views': self.views if self.views else 0,
        }


class UpdateInfo(Base):
    '''
    只有一条记录

    content 是所有已经爬取过的页面的 URL 列表
    '''
    __tablename__ = 'fish_update_info'

    update_id = sa.Column(
        sa.Integer,
        primary_key=True,
    )
    content = sa.Column(
        sa.ARRAY(sa.String),
    )
    last_update_time = sa.Column(
        sa.DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
    )

    def __repr__(self):
        return "<UpdateInfo(last_update_time='%s')>" % (
            self.last_update_time.strftime('%Y-%m-%d %H:%M:%S')
        )
