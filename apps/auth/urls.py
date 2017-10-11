# coding=utf-8

from flask import Blueprint

from apps.auth import views


bp = Blueprint('auth', __name__, url_prefix='/auth')

bp.add_url_rule('/login', view_func=views.Login.as_view('login'))
bp.add_url_rule('/logout', view_func=views.Logout.as_view('logout'))
