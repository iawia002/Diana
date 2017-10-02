# coding=utf-8

from flask import Blueprint

from apps.fish import views


bp = Blueprint('fish', __name__, url_prefix='/fish')

bp.add_url_rule('/', view_func=views.Index.as_view('index'))
bp.add_url_rule(
    '/p/<int:record_id>', view_func=views.Article.as_view('article')
)
bp.add_url_rule('/more', view_func=views.More.as_view('more'))
