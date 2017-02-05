#!/usr/bin/env python
# coding=utf-8


import config
import utils.db
import utils.tags
import utils.auth
import utils.common
import utils.json_utils
from db.sa import Session
from apps.model import (
    User,
    Tag as TagModel,
)
from apps.base import BaseHandler


class Tag(BaseHandler):
    def get(self, tag):
        session = Session()
        tag = utils.tags.tag_url_decode(tag)
        t = session.query(TagModel).filter(TagModel.content == tag).first()
        if not t:
            return utils.common.raise_error(request=self, status_code=404)
        articles = utils.db.tag_articles(
            tag=tag, page=1, user_id=config.USER_ID
        )
        data = {}
        data['tag'] = tag
        data['articles'] = articles
        user = utils.db.user(user_id=config.USER_ID)
        data['user'] = user
        data['next_page'] = 2
        session.commit()
        session.close()
        self.render('tag.html', data=data)


class Tags(BaseHandler):
    def get(self):
        session = Session()
        tags = session.query(User).filter(
            User.user_id == config.USER_ID
        ).first().tag
        tags = [tag.to_json() for tag in tags]
        session.commit()
        session.close()
        tags_keys = [
            utils.tags.single_get_first(
                tag['content'][0]
            ) for tag in tags
        ]
        tags_keys = list(set(tags_keys))
        kv = {}
        for key in tags_keys:
            kv[key] = []

        for tag in tags:
            kv[utils.tags.single_get_first(
                tag['content'][0]
            )].append(tag)

        for value in kv:
            kv[value].sort(key=lambda x: x['content'])

        values = sorted(kv.iteritems(), key=lambda x: x[0])
        keys = kv.keys()
        keys.sort()

        data = {}
        data['keys'] = keys
        data['values'] = values
        user = utils.db.user(user_id=config.USER_ID)
        data['user'] = user
        self.render('tags.html', data=data)
