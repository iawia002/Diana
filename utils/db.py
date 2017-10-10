#!/usr/bin/env python
# coding=utf-8

from sqlalchemy.sql import ClauseElement

import config
from apps.blog.models import (
    Tag,
    User,
)


def get_instance(session, model, defaults=None, commit=False, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        params = dict(
            (k, v) for k, v in kwargs.items()
            if not isinstance(v, ClauseElement)
        )
        params.update(defaults or {})
        instance = model(**params)
        if commit:
            session.add(instance)
            session.commit()
        return instance


def get_or_create(session, model, defaults=None, **kwargs):
    return get_instance(
        session, model, defaults=defaults, commit=True, **kwargs
    )


def user(user_id):
    user = User.query.filter_by(
        user_id=user_id
    ).first().to_json()
    return user


def articles_to_json(articles):
    return [article.to_json() for article in articles]


def article(page, user_id):
    '''
    page 从 1 开始
    '''
    page = int(page)
    articles = User.query.filter_by(
        user_id=user_id
    ).first().article[
        (page-1)*config.ARTICLE_PAGE_NUMBER: page*config.ARTICLE_PAGE_NUMBER
    ]
    articles = articles_to_json(articles)
    return articles


def tag_articles(tag, page, user_id):
    page = int(page)
    user = User.query.filter_by(
        user_id=user_id
    ).first()
    tag = Tag.query.filter_by(
        content=tag
    ).first()
    if user not in tag.user:
        return None
    articles = tag.article[
        (page-1)*config.ARTICLE_PAGE_NUMBER: page*config.ARTICLE_PAGE_NUMBER
    ]
    articles = articles_to_json(articles)
    return articles
