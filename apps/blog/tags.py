#!/usr/bin/env python
# coding=utf-8

from flask import (
    render_template,
)
from flask.views import MethodView

import config
import utils.db
import utils.tags
import utils.auth
import utils.common
import utils.json_utils
from db.sa import Session
from apps.blog.models import (
    User,
    Tag as TagModel,
)


class Tag(MethodView):
    @utils.auth.login_status
    def get(self, tag):
        session = Session()
        tag = utils.tags.tag_url_decode(tag)
        t = session.query(TagModel).filter_by(content=tag).first()
        if not t:
            return utils.common.raise_error(status_code=404)
        articles = utils.db.tag_articles(
            tag=tag, page=1, user_id=config.USER_ID
        )
        data = {}
        data['tag'] = tag
        data['articles'] = articles
        user = utils.db.user(user_id=config.USER_ID)
        data['user'] = user
        data['next_page'] = 2
        data['login'] = self.login
        session.commit()
        session.close()
        return render_template('blog/tag.html', data=data)


class Tags(MethodView):
    def get(self):
        session = Session()
        tags = session.query(User).filter_by(
            user_id=config.USER_ID
        ).first().tag
        # 所有标签要排除空标签
        tags = [tag.to_json() for tag in tags if len(tag.article.all()) > 0]
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

        values = sorted(kv.items(), key=lambda x: x[0])
        keys = sorted(kv.keys())

        data = {}
        data['keys'] = keys
        data['values'] = values
        user = utils.db.user(user_id=config.USER_ID)
        data['user'] = user
        return render_template('blog/tags.html', data=data)
