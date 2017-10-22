# coding=utf-8

import datetime

from main import db
from models.base import CreateTimeMixin


class Record(CreateTimeMixin, db.Model):
    '''
    所有钓鱼帖的记录
    '''
    __tablename__ = 'fish_record'

    record_id = db.Column(
        db.Integer,
        primary_key=True,
    )
    title = db.Column(
        db.String(100),
    )
    content = db.Column(
        db.ARRAY(db.String),
    )
    image_num = db.Column(
        db.Integer,
    )
    source = db.Column(
        db.String(1000),
    )
    views = db.Column(
        db.Integer,
        default=0,
    )
    update_time = db.Column(
        # 不能自动更新，因为每次访问 views 都会更新，会导致更新时间也变化
        db.DateTime,
        default=datetime.datetime.now,
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


class UpdateInfo(db.Model):
    '''
    只有一条记录

    content 是所有已经爬取过的页面的 URL 列表
    '''
    __tablename__ = 'fish_update_info'

    update_id = db.Column(
        db.Integer,
        primary_key=True,
    )
    content = db.Column(
        db.ARRAY(db.String),
    )
    last_update_time = db.Column(
        db.DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
    )

    def __repr__(self):
        return "<UpdateInfo(last_update_time='%s')>" % (
            self.last_update_time.strftime('%Y-%m-%d %H:%M:%S')
        )
