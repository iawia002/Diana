#!/usr/bin/env python
# coding=utf-8

from apps import model
from db.sa import Session


def init_user():
    session = Session()
    user = model.User(
        user_id=1,
        username='admin',
        password='$2b$12$LnGoWYDTBQ6yryO94dOEd.fXyZJXn8OFUIixaJXseViK2dQTt8X9G',  # noqa
        avatar='http://img.l.jifangcheng.com/Katarina.png',
        introduction='hello',
    )
    session.add(user)
    session.commit()
    session.close()


def init_article():
    session = Session()
    article = model.Article(
        user_id=1,
        title='hello',
        introduction='<p>hello</p>',
        markdown_content='''
# hello
> hello

hello
        ''',
        compiled_content='''
<h1 id="hello">hello</h1>
<blockquote>
<p>hello</p>
</blockquote>
<p>hello</p>
        ''',
    )
    session.add(article)
    session.commit()
    session.close()


if __name__ == '__main__':
    init_user()
    init_article()
