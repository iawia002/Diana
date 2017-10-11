# coding=utf-8

import datetime

from main import db


user_tag = db.Table(
    'user_tag',
    db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('users.user_id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.tag_id')),
)


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(
        db.Integer,
        primary_key=True,
    )
    username = db.Column(
        db.String(100),
        nullable=False,
        unique=True,
    )
    password = db.Column(
        db.String(128),
        nullable=False,
    )
    avatar = db.Column(
        db.String(200),
    )
    introduction = db.Column(
        db.String(100),
        nullable=False,
    )
    join_time = db.Column(
        db.DateTime,
        default=datetime.datetime.now,
    )
    last_login = db.Column(
        db.DateTime,
        default=datetime.datetime.now,
    )
    tag = db.relationship(
        'apps.blog.models.Tag',
        secondary=user_tag,
        back_populates='user',
    )
    article = db.relationship(
        'apps.blog.models.Article',
        back_populates='user',
        order_by='desc(apps.blog.models.Article.create_time)',
        lazy='dynamic',
    )

    def __repr__(self):
        return '<User(name={})>'.format(self.username)

    def to_json(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'avatar': self.avatar,
            'introduction': self.introduction,
            'join_time': self.join_time,
            'last_login': self.last_login,
        }
