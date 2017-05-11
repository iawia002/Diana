#!/usr/bin/env python
# coding=utf-8

import utils.common
from db.sa import Session
from apps.fish import db_utils
from apps.base import BaseHandler
from apps.fish.models import Record


class Index(BaseHandler):
    def get(self):
        data = {}
        articles = db_utils.article(page=1)
        data['articles'] = articles
        data['next_page'] = 2
        self.render('fish/index.html', data=data)


class More(BaseHandler):
    def get(self):
        next_page = self.get_argument('next_page')
        try:
            next_page = int(next_page)
        except ValueError:
            return self.write('')
        articles = db_utils.article(page=next_page)

        if not articles:
            return self.write('')
        data = {}
        data['articles'] = articles
        article_list = self.render_string('fish/article_list.html', data=data)
        ret = {
            'next_page': next_page + 1,
            'data': article_list
        }
        self.write(ret)


class Article(BaseHandler):
    def get(self, record_id):
        session = Session()
        article = session.query(Record).filter(
            Record.record_id == record_id,
        ).first()
        if not article:
            return utils.common.raise_error(request=self, status_code=404)
        # 兼容以前的数据
        if not article.views:
            article.views = 0
        # 更新浏览次数
        article.views += 1
        session.add(article)
        session.commit()
        article_data = article.json
        session.close()
        data = {}
        data['article'] = article_data
        self.render('fish/article.html', data=data)
