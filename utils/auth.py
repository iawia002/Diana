# coding=utf-8

from flask import (
    session,
    redirect,
)


def login_require(func):
    def wrapper(*args, **kwargs):
        self = args[0]
        user_id = session.get('diana')
        if user_id:
            self.user_id = user_id
            return func(*args, **kwargs)
        else:
            return redirect('/')
    return wrapper


def login_status(func):
    def wrapper(*args, **kwargs):
        self = args[0]
        self.login = False
        if 'diana' in session:
            self.login = True
        return func(*args, **kwargs)
    return wrapper
