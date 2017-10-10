#!/usr/bin/env python
# coding=utf-8

import random
import datetime

from flask import (
    jsonify,
    request,
    render_template,
)
from flask.views import MethodView

import utils.db
import utils.tags
import utils.auth
import utils.common
import utils.json_utils

import config
from main import db
from apps.blog.models import (
    Tag,
    User,
    Article as ArticleModel,
)


class Index(MethodView):
    @utils.auth.login_status
    def get(self):
        data = {}
        data['bg'] = random.choice(config.INDEX_BG)
        data['last_article'] = User.query.filter_by(
            user_id=config.USER_ID
        ).first().article[0]
        if data['last_article']:
            data['last_article'] = data['last_article'].to_json()

        articles = utils.db.article(page=1, user_id=config.USER_ID)
        user = utils.db.user(user_id=config.USER_ID)
        data['articles'] = articles
        data['user'] = user
        data['next_page'] = 2
        data['login'] = self.login
        return render_template('blog/index.html', data=data)


class More(MethodView):
    @utils.auth.login_status
    def get(self):
        next_page = request.args.get('next_page')
        page = request.args.get('page')
        tag = request.args.get('tag')

        articles = None
        if page == 'index':
            articles = utils.db.article(page=next_page, user_id=config.USER_ID)
        elif page == 'tag':
            articles = utils.db.tag_articles(
                tag=tag, page=next_page, user_id=config.USER_ID
            )

        if not articles:
            return ''
        # articles = utils.tags.articles_add_tags(articles)
        data = {}
        data['articles'] = articles
        data['login'] = self.login
        article_list = render_template(
            'blog/article_list.html', data=data
        )
        ret = {
            'next_page': int(next_page) + 1,
            'data': article_list
        }
        return jsonify(ret)


class Article(MethodView):
    @utils.auth.login_status
    def get(self, article_id):
        article = ArticleModel.query.filter_by(
            article_id=article_id,
            user_id=config.USER_ID
        ).first()
        if not article:
            return utils.common.raise_error(status_code=404)
        # 兼容以前的数据
        if not article.views:
            article.views = 0
        # 更新浏览次数
        article.views += 1
        db.session.add(article)
        db.session.commit()
        article = article.to_json()
        user = utils.db.user(user_id=config.USER_ID)
        data = {}
        data['article'] = article
        data['user'] = user
        data['login'] = self.login
        return render_template('blog/article.html', data=data)


class Edit(MethodView):
    @utils.auth.login_require
    def get(self, article_id):
        data = {}
        article = ArticleModel.query.filter_by(
            article_id=article_id,
            user_id=self.user_id
        ).first()
        if article:
            article = article.to_json()
            data['article_markdown_content'] = article['markdown_content']
            data['article_title'] = article['title']
        else:
            data['article_markdown_content'] = ''
            data['article_title'] = ''
        data['article_id'] = article_id
        return render_template('blog/editor.html', data=data)

    @utils.auth.login_require
    def post(self, article_id):
        article_id = int(article_id)
        data = {
            'title': request.form.get('title'),
            'introduction': request.form.get('introduction'),
            'markdown_content': request.form.get('markdown_content'),
            'compiled_content': request.form.get('compiled_content'),
            'user_id': self.user_id,
        }
        tags = request.form.getlist('tags[]')

        user = User.query.filter_by(
            user_id=self.user_id
        ).first()
        article = ArticleModel.query.filter_by(
            article_id=article_id,
            user_id=self.user_id
        ).first()
        if article:
            data.update({'update_time': datetime.datetime.now()})
            for k, v in data.items():
                setattr(article, k, v)
        else:
            article = ArticleModel(**data)

        # 文章标签更新方法：先把以前的全部删除再全部新建
        article.tag[:] = []
        for tag in tags:
            tag = utils.db.get_or_create(db.session, Tag, content=tag)
            article.tag.append(tag)
            user.tag.append(tag)
        db.session.add(user)
        db.session.add(article)
        db.session.commit()
        return ''
