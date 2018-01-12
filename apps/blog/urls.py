# coding=utf-8

from flask import Blueprint

from apps.blog import views

bp = Blueprint('blog', __name__)

bp.add_url_rule('/', view_func=views.IndexView.as_view('index'))
bp.add_url_rule(
    '/p/<int:article_id>', view_func=views.ArticleView.as_view('article')
)
bp.add_url_rule(
    '/p/<int:article_id>/edit',
    view_func=views.EditView.as_view('article_edit')
)
bp.add_url_rule('/more', view_func=views.MoreView.as_view('more'))
bp.add_url_rule('/tag/<string:tag>', view_func=views.TagView.as_view('tag'))
bp.add_url_rule('/tags', view_func=views.TagsView.as_view('tags'))
bp.add_url_rule('/user', view_func=views.UserView.as_view('user'))
bp.add_url_rule(
    '/statistics', view_func=views.StatisticsView.as_view('statistics')
)
