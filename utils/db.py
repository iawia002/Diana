#!/usr/bin/env python
# coding=utf-8

from __future__ import absolute_import

from sqlalchemy.sql import ClauseElement

import config
from db.sa import Session
from apps.model import (
    Tag,
    User,
)


def get_or_create(session, model, defaults=None, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        params = dict(
            (k, v) for k, v in kwargs.iteritems()
            if not isinstance(v, ClauseElement)
        )
        params.update(defaults or {})
        instance = model(**params)
        session.add(instance)
        session.commit()
        return instance


def user(user_id):
    session = Session()
    user = session.query(User).filter(
        User.user_id == user_id
    ).first().to_json()
    session.commit()
    session.close()
    return user


def articles_to_json(articles):
    return [article.to_json() for article in articles]


def article(page, user_id):
    '''
    page 从 1 开始
    '''
    page = int(page)
    session = Session()
    articles = session.query(User).filter(
        User.user_id == user_id
    ).first().article[
        (page-1)*config.ARTICLE_PAGE_NUMBER: page*config.ARTICLE_PAGE_NUMBER
    ]
    articles = articles_to_json(articles)
    session.commit()
    session.close()
    return articles


def tag_articles(tag, page, user_id):
    page = int(page)
    session = Session()
    user = session.query(User).filter(
        User.user_id == user_id
    ).first()
    tag = session.query(Tag).filter(
        Tag.content == tag
    ).first()
    if user not in tag.user:
        return None
    articles = tag.article[
        (page-1)*config.ARTICLE_PAGE_NUMBER: page*config.ARTICLE_PAGE_NUMBER
    ]
    articles = articles_to_json(articles)
    session.commit()
    session.close()
    return articles
