# coding=utf-8

from flask import Blueprint

from apps.fun import views


bp = Blueprint('fun', __name__, url_prefix='/fun')

bp.add_url_rule('/', view_func=views.Index.as_view('index'))
