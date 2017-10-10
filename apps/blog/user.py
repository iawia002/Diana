# coding=utf-8

from flask import (
    request,
)
from flask.views import MethodView

from main import db
from utils.auth import login_require
from apps.blog.models import User as UserModel


class User(MethodView):

    @login_require
    def post(self):
        user = UserModel.query.filter_by(
            user_id=self.user_id
        ).first()
        introduction = request.form.get('introduction')
        if not introduction:
            return '', 400
        user.introduction = introduction
        db.session.add(user)
        db.session.commit()
        return ''
