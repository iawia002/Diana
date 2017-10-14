# coding=utf-8

from flask import Blueprint

from apps.blog import (
    blog,
    statistics,
    tags,
    user,
)

bp = Blueprint('blog', __name__)

bp.add_url_rule('/', view_func=blog.Index.as_view('index'))
bp.add_url_rule(
    '/p/<int:article_id>', view_func=blog.Article.as_view('article')
)
bp.add_url_rule(
    '/p/<int:article_id>/edit', view_func=blog.Edit.as_view('article_edit')
)
bp.add_url_rule('/more', view_func=blog.More.as_view('more'))
bp.add_url_rule('/tag/<string:tag>', view_func=tags.Tag.as_view('tag'))
bp.add_url_rule('/tags', view_func=tags.Tags.as_view('tags'))
bp.add_url_rule('/user', view_func=user.User.as_view('user'))
bp.add_url_rule(
    '/statistics', view_func=statistics.Statistics.as_view('statistics')
)
