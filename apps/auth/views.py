# coding=utf-8

import bcrypt
from flask import (
    session,
    request,
    redirect,
    render_template,
)
from flask.views import MethodView

from apps.auth.models import User


class Login(MethodView):
    '''
    登录页面
    '''
    def get(self):
        return render_template('auth/login.html')

    def post(self):
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(
            username=username
        ).first()
        if user and bcrypt.checkpw(
            password.encode('utf-8'), user.password.encode('utf-8')
        ):
            session.permanent = True
            session['diana'] = str(user.user_id)
            return redirect('/')
        else:
            return redirect('/'), 400


class Logout(MethodView):
    '''
    登出
    '''
    def get(self):
        session.pop('diana', None)
        return redirect('/')
