# coding=utf-8

from flask import (
    request,
)
from flask.views import MethodView

from db.sa import Session
from utils.auth import login_require
from apps.blog.models import User as UserModel


class User(MethodView):

    @login_require
    def post(self):
        session = Session()
        user = session.query(UserModel).filter_by(
            user_id=self.user_id
        ).first()
        introduction = request.form.get('introduction')
        if not introduction:
            return '', 400
        user.introduction = introduction
        session.add(user)
        session.commit()
        return ''
