#!/usr/bin/env python
# coding=utf-8

from itertools import groupby

from sqlalchemy.sql import (
    func,
)

from db.sa import Session
from utils.auth import login_require
from apps.model import (
    Article,
    AccessLog as AccessLogModel,
)

from apps.base import BaseHandler


class AccessLog(BaseHandler):
    def prepare(self):
        super(AccessLog, self).prepare()
        self.session = Session()

    def get_article_info(self, access_log):
        uri = access_log.uri
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

    def get_session(self):
        modules = ['Article', 'Tag', 'Tags', 'Index']
        return self.session.query(AccessLogModel).filter(
            AccessLogModel.module.in_(modules)
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
        max_views = self.session.query(AccessLogModel).filter_by(
            views=self.session.query(func.max(AccessLogModel.views))
        ).all()
        # 最多访问数可能有并列最多的
        max_view_data = {
            'views': max_views[0].views,
            'data': []
        }
        for record in max_views:
            max_view_data['data'].append(
                self.get_article_info(record)
            )

        max_persons = []
        # 总共不重复的页面
        uri = self.session.query(AccessLogModel.uri).group_by(
            AccessLogModel.uri
        ).all()
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
                    self.get_article_info(item.first())
                )
            # 只取第一项（个数最多的那一项），不能对 groupby 进行 list 操作
            break

        data.update({
            'max_views': max_view_data,
            'max_persons': max_person_data,
        })
        self.session.close()
        return self.write(data)
