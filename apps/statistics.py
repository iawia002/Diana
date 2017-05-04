#!/usr/bin/env python
# coding=utf-8

from itertools import groupby

from sqlalchemy.sql import (
    func,
)

import config
import utils.db
from db.sa import Session
from utils.auth import login_require
from apps.model import (
    Article,
    AccessLog as AccessLogModel,
)

from apps.base import BaseHandler


class Statistics(BaseHandler):
    def initialize(self):
        self.session = Session()
        self.modules = ['Article', 'Tag', 'Tags', 'Index']
        self.queryset = self.get_queryset()

    def get_article_info(self, uri):
        article_id = uri.split('/')[-1]
        try:
            article_id = int(article_id)
            title = self.session.query(Article).filter_by(
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

    def get_queryset(self):
        return self.session.query(AccessLogModel).filter(
            AccessLogModel.module.in_(self.modules)
        )

    @login_require
    def get(self):
        data = {
            'unique_visitors': self.session.query(AccessLogModel).distinct(
                AccessLogModel.remote_ip,
            ).count(),
            'views': self.session.query(
                func.sum(AccessLogModel.views)
            ).scalar(),
        }
        # 总共不重复的页面
        uri = self.session.query(AccessLogModel.uri).group_by(
            AccessLogModel.uri
        ).all()

        max_views = []
        # 最多访问数可能有并列最多的
        max_view_data = {
            'views': '',
            'data': []
        }
        for item in uri:
            max_views.append({
                'views': self.session.query(
                    func.sum(AccessLogModel.views)
                ).filter_by(uri=item).scalar(),
                'uri': item[0],
            })
        # 排序，按个数分组
        max_views.sort(reverse=True, key=lambda x: x['views'])
        max_views_group = groupby(max_views, lambda x: x['views'])
        for key, group in max_views_group:
            max_view_data['views'] = key
            for item in group:
                max_view_data['data'].append(
                    self.get_article_info(item['uri'])
                )
            # 只取第一项（个数最多的那一项），不能对 groupby 进行 list 操作
            break

        max_persons = []
        for item in uri:
            max_persons.append(
                # 每个页面不重复的访问人数
                self.session.query(AccessLogModel).filter_by(
                    uri=item
                ).distinct(AccessLogModel.remote_ip)
            )

        # 排序，按个数分组
        max_persons.sort(key=lambda x: x.count(), reverse=True)
        max_person_group = groupby(max_persons, lambda x: x.count())
        max_person_data = {
            'views': '',
            'data': [],
        }
        for key, group in max_person_group:
            max_person_data['views'] = key
            for item in group:
                max_person_data['data'].append(
                    self.get_article_info(item.first().uri)
                )
            # 只取第一项（个数最多的那一项），不能对 groupby 进行 list 操作
            break

        data.update({
            'max_views': max_view_data,
            'max_persons': max_person_data,
        })
        self.session.close()
        data['user'] = utils.db.user(user_id=config.USER_ID)
        return self.render('statistics.html', data=data)
