# coding=utf-8

import bcrypt
from flask import (
    request,
    redirect,
    render_template,
    session as flask_session,
)
from flask.views import MethodView

from db.sa import Session
from apps.blog.models import User


class Login(MethodView):
    '''
    登录页面
    '''
    def get(self):
        return render_template('blog/login.html')

    def post(self):
        session = Session()
        username = request.form['username']
        password = request.form['password']
        user = session.query(User).filter_by(
            username=username
        ).first()
        if user and bcrypt.checkpw(
            password.encode('utf-8'), user.password.encode('utf-8')
        ):
            flask_session.permanent = True
            flask_session['diana'] = str(user.user_id)
            return redirect('/')
        else:
            return redirect('/'), 400


class Logout(MethodView):
    '''
    登出
    '''
    def get(self):
        flask_session.pop('diana', None)
        return redirect('/')
