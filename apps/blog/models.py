# coding=utf-8

import datetime

import utils.tags
from main import db


'''
用户和文章是一对多关系，一个用户可以有很多文章，一篇文章只能有一个用户
用户和标签是多对多关系，一个用户可以有很多标签，一个标签也可以有很多用户
文章和标签是多对多关系，一篇文章可以有很多标签，一个标签也可以有很多文章

标签表只有 id 和 content
'''

tag_article = db.Table(
    'tag_article',
    db.Model.metadata,
    db.Column('article_id', db.Integer, db.ForeignKey('article.article_id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.tag_id')),
)

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


class Article(db.Model):
    __tablename__ = 'article'

    article_id = db.Column(
        db.Integer,
        primary_key=True,
    )
    title = db.Column(
        db.String(100)
        # db.Unicode(100)
    )
    markdown_content = db.Column(
        db.Text
        # db.UnicodeText
    )
    create_time = db.Column(
        db.DateTime,
        default=datetime.datetime.now,
    )
    update_time = db.Column(
        db.DateTime,
        default=datetime.datetime.now,
    )
    introduction = db.Column(
        db.String(1000)
    )
    compiled_content = db.Column(
        db.Text
    )
    views = db.Column(
        db.Integer,
        default=0,
    )
    user = db.relationship(
        'apps.blog.models.User',
        back_populates='article',
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.user_id'),
    )
    tag = db.relationship(
        'apps.blog.models.Tag',
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


class Tag(db.Model):
    __tablename__ = 'tags'

    tag_id = db.Column(
        db.Integer,
        primary_key=True,
    )
    content = db.Column(
        db.String(100),
        unique=True,
    )
    create_time = db.Column(
        db.DateTime,
        default=datetime.datetime.now,
    )
    article = db.relationship(
        'apps.blog.models.Article',
        secondary=tag_article,
        back_populates='tag',
        order_by='desc(apps.blog.models.Article.create_time)',
        lazy='dynamic',
    )
    user = db.relationship(
        'apps.blog.models.User',
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
