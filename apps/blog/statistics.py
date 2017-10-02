# coding=utf-8

from itertools import groupby

from sqlalchemy.sql import (
    func,
)
from flask import (
    render_template,
)
from flask.views import MethodView

import config
import utils.db
from db.sa import Session
from utils.auth import login_require
from apps.blog.models import Article
from models.statistics import AccessLog as AccessLogModel


class Statistics(MethodView):
    def __init__(self):
        self.session = Session()

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
        uri = self.session.query(AccessLogModel.uri).group_by(
            AccessLogModel.uri
        ).all()
        # 最多访问数可能有并列最多的
        page_data = []
        for item in uri:
            persons = self.session.query(AccessLogModel).filter_by(
                uri=item
            ).distinct(AccessLogModel.remote_ip)
            page_data.append({
                'uri': item[0],
                'views': self.session.query(
                    func.sum(AccessLogModel.views)
                ).filter_by(uri=item).scalar(),
                'persons': persons.count(),
                'person_instance': persons,
            })

        # 排序，按个数分组
        page_data.sort(reverse=True, key=lambda x: x['views'])
        max_views_group = groupby(page_data, lambda x: x['views'])
        max_view_data = self.generate_group_data(max_views_group, 'persons')

        page_data.sort(key=lambda x: x['persons'], reverse=True)
        max_persons_group = groupby(page_data, lambda x: x['persons'])
        max_persons_data = self.generate_group_data(max_persons_group, 'views')
        return max_view_data, max_persons_data

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
        page_data = self.get_page_data()
        data.update({
            'max_views': page_data[0],
            'max_persons': page_data[1],
        })
        self.session.close()
        data['user'] = utils.db.user(user_id=config.USER_ID)
        return render_template('blog/statistics.html', data=data)
