# coding=utf-8

import random
import datetime
from itertools import groupby

from flask import (
    jsonify,
    request,
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
    Article,
)
from apps.auth.models import User
from models.statistics import AccessLog


class IndexView(MethodView):
    @utils.auth.login_status
    def get(self):
        data = {}
        data['bg'] = random.choice(config.INDEX_BG)
        articles = utils.db.article(page=1, user_id=config.USER_ID)
        user = utils.db.user(user_id=config.USER_ID)
        data['articles'] = articles
        data['user'] = user
        data['next_page'] = 2
        data['login'] = self.login
        return jsonify(data)


class MoreView(MethodView):
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
            return jsonify({})
        ret = {
            'articles': articles,
            'next_page': int(next_page) + 1,
            'login': self.login,
        }
        return jsonify(ret)


class ArticleView(MethodView):
    @utils.auth.login_status
    def get(self, article_id):
        article = Article.query.filter_by(
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
        return jsonify(data)


class EditView(MethodView):
    @utils.auth.login_require
    def get(self, article_id):
        data = {}
        article = Article.query.filter_by(
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
        return jsonify(data)

    @utils.auth.login_require
    def post(self, article_id):
        article_id = int(article_id)
        data = {
            'title': request.json.get('title'),
            'introduction': request.json.get('introduction'),
            'markdown_content': request.json.get('markdown_content'),
            'compiled_content': request.json.get('compiled_content'),
            'user_id': self.user_id,
        }
        tags = request.json.get('tags')

        user = User.query.filter_by(
            user_id=self.user_id
        ).first()
        article = Article.query.filter_by(
            article_id=article_id,
            user_id=self.user_id
        ).first()
        if article:
            data.update({'update_time': datetime.datetime.now()})
            for k, v in data.items():
                setattr(article, k, v)
        else:
            article = Article(**data)

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


class TagView(MethodView):
    @utils.auth.login_status
    def get(self, tag):
        tag = utils.tags.tag_url_decode(tag)
        t = Tag.query.filter_by(content=tag).first()
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
        return jsonify(data)


class TagsView(MethodView):
    def get(self):
        tags = User.query.filter_by(
            user_id=config.USER_ID
        ).first().tag
        # 所有标签要排除空标签
        tags = [tag.to_json() for tag in tags if len(tag.article.all()) > 0]
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
        return jsonify(data)


class UserView(MethodView):

    @utils.auth.login_require
    def post(self):
        user = User.query.filter_by(
            user_id=self.user_id
        ).first()
        introduction = request.form.get('introduction')
        if not introduction:
            return '', 400
        user.introduction = introduction
        db.session.add(user)
        db.session.commit()
        return ''


class StatisticsView(MethodView):
    def get_article_info(self, uri):
        article_id = uri.split('/')[-1]
        try:
            article_id = int(article_id)
            title = Article.query.filter_by(
                article_id=article_id
            ).first().title
        except Exception:
            if uri == '/':
                title = 'L'
            else:
                title = uri
        return {
            'uri': uri,
            'title': title,
        }

    def generate_group_data(self, group, extra_data_type):
        data = {
            'views': '',
            'data': []
        }
        for key, group in group:
            data['views'] = key
            for item in group:
                temp = self.get_article_info(item['uri'])
                temp.update({
                    extra_data_type: item[extra_data_type]
                })
                data['data'].append(temp)
            # 只取第一项（个数最多的那一项），不能对 groupby 进行 list 操作
            break
        return data

    def get_page_data(self):
        # 总共不重复的页面
        uri = db.session.query(AccessLog.uri).group_by(
            AccessLog.uri
        ).all()
        # 最多访问数可能有并列最多的
        page_data = []
        for item in uri:
            persons = db.session.query(AccessLog).filter_by(
                uri=item
            ).distinct(AccessLog.remote_ip)
            page_data.append({
                'uri': item[0],
                'views': db.session.query(AccessLog).filter_by(
                    uri=item
                ).count(),
                'persons': persons.count(),
                'person_instance': persons,
            })

        # 排序，按个数分组
        page_data.sort(key=lambda x: x['views'], reverse=True)
        max_views_group = groupby(page_data, lambda x: x['views'])
        max_view_data = self.generate_group_data(max_views_group, 'persons')

        page_data.sort(key=lambda x: x['persons'], reverse=True)
        max_persons_group = groupby(page_data, lambda x: x['persons'])
        max_persons_data = self.generate_group_data(max_persons_group, 'views')
        return max_view_data, max_persons_data

    @utils.auth.login_require
    def get(self):
        data = {
            'unique_visitors': db.session.query(AccessLog).distinct(
                AccessLog.remote_ip,
            ).count(),
            'views': db.session.query(AccessLog).count(),
        }
        page_data = self.get_page_data()
        data.update({
            'max_views': page_data[0],
            'max_persons': page_data[1],
        })
        data['user'] = utils.db.user(user_id=config.USER_ID)
        return jsonify(data)
