#!/usr/bin/env python
# coding=utf-8

from db.sa import Session
from utils.auth import login_require
from apps.blog.models import User as UserModel

from apps.base import BaseHandler


class User(BaseHandler):

    @login_require
    def post(self):
        session = Session()
        user = session.query(UserModel).filter_by(
            user_id=self.user_id
        ).first()
        introduction = self.get_argument('introduction')
        if not introduction:
            self.set_status(400)
            return self.write('')
        user.introduction = introduction
        session.add(user)
        session.commit()
        return self.write('')
