#!/usr/bin/env python
# coding=utf-8

import bcrypt

from db.sa import Session
from apps.base import BaseHandler
from apps.blog.models import User


class Login(BaseHandler):

    '''登录页面'''

    def get(self):
        return self.render('blog/login.html')

    def post(self):
        session = Session()
        username = self.get_argument('username')
        password = self.get_argument('password')
        user = session.query(User).filter_by(username=username).first()
        if user and bcrypt.checkpw(
            password.encode('utf-8'), user.password.encode('utf-8')
        ):
            self.set_secure_cookie('diana', str(user.user_id))
            self.redirect('/')
        else:
            self.redirect('/')


class Logout(BaseHandler):

    '''登出页面'''

    def get(self):
        self.clear_all_cookies()
        self.redirect('/')
