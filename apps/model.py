#!/usr/bin/env python
# coding=utf-8

import datetime

import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

import utils.tags

Base = declarative_base()

'''
用户和文章是一对多关系，一个用户可以有很多文章，一篇文章只能有一个用户
用户和标签是多对多关系，一个用户可以有很多标签，一个标签也可以有很多用户
文章和标签是多对多关系，一篇文章可以有很多标签，一个标签也可以有很多文章

标签表只有 id 和 content
'''

tag_article = sa.Table(
    'tag_article',
    Base.metadata,
    sa.Column('article_id', sa.Integer, sa.ForeignKey('article.article_id')),
    sa.Column('tag_id', sa.Integer, sa.ForeignKey('tags.tag_id')),
)

user_tag = sa.Table(
    'user_tag',
    Base.metadata,
    sa.Column('user_id', sa.Integer, sa.ForeignKey('users.user_id')),
    sa.Column('tag_id', sa.Integer, sa.ForeignKey('tags.tag_id')),
)


class User(Base):
    __tablename__ = 'users'

    user_id = sa.Column(
        sa.Integer,
        primary_key=True,
    )
    username = sa.Column(
        sa.String(100),
        nullable=False,
        unique=True,
    )
    password = sa.Column(
        sa.String(128),
        nullable=False,
    )
    avatar = sa.Column(
        sa.String(200),
    )
    introduction = sa.Column(
        sa.String(100),
        nullable=False,
    )
    join_time = sa.Column(
        sa.DateTime,
        default=datetime.datetime.now,
    )
    last_login = sa.Column(
        sa.DateTime,
        default=datetime.datetime.now,
    )
    tag = relationship(
        'Tag',
        secondary=user_tag,
        back_populates='user',
    )
    article = relationship(
        'Article',
        back_populates='user',
        order_by='desc(Article.create_time)',
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


class Article(Base):
    __tablename__ = 'article'

    article_id = sa.Column(
        sa.Integer,
        primary_key=True,
    )
    title = sa.Column(
        sa.String(100)
        # sa.Unicode(100)
    )
    markdown_content = sa.Column(
        sa.Text
        # sa.UnicodeText
    )
    create_time = sa.Column(
        sa.DateTime,
        default=datetime.datetime.now,
    )
    update_time = sa.Column(
        sa.DateTime,
        default=datetime.datetime.now,
    )
    introduction = sa.Column(
        sa.String(1000)
    )
    compiled_content = sa.Column(
        sa.Text
    )
    views = sa.Column(
        sa.Integer,
        default=0,
    )
    user = relationship(
        'User',
        back_populates='article',
    )
    user_id = sa.Column(
        sa.Integer,
        sa.ForeignKey('users.user_id'),
    )
    tag = relationship(
        'Tag',
        secondary=tag_article,
        back_populates='article',
    )

    def __repr__(self):
        return '<Article(title={})>'.format(self.title)

    def to_json(self):
        tags = [i.to_json() for i in self.tag]
        return {
            'article_id': self.article_id,
            'user_id': self.user_id,
            'title': self.title,
            'markdown_content': self.markdown_content,
            'create_time': datetime.datetime.strftime(
                self.create_time, '%Y-%m-%d %H:%M:%S'
            ),
            'update_time': datetime.datetime.strftime(
                self.update_time, '%Y-%m-%d %H:%M:%S'
            ),
            'introduction': self.introduction,
            'compiled_content': self.compiled_content,
            'tags': tags,
            'views': self.views if self.views else 0,
        }


class Tag(Base):
    __tablename__ = 'tags'

    tag_id = sa.Column(
        sa.Integer,
        primary_key=True,
    )
    content = sa.Column(
        sa.String(100),
        unique=True,
    )
    create_time = sa.Column(
        sa.DateTime,
        default=datetime.datetime.now,
    )
    article = relationship(
        'Article',
        secondary=tag_article,
        back_populates='tag',
        order_by='desc(Article.create_time)',
        lazy='dynamic',
    )
    user = relationship(
        'User',
        secondary=user_tag,
        back_populates='tag',
    )

    def __repr__(self):
        return '<Tag(content={})>'.format(self.content.encode('utf-8'))

    def to_json(self):
        return {
            'tag_id': self.tag_id,
            'content': self.content,
            'create_time': self.create_time,
            'number': len(self.article.all()),
            'url': utils.tags.tag_url_encode(self.content),
        }


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
    module = sa.Column(
        sa.String(10),
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
