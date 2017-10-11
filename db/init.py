#!/usr/bin/env python
# coding=utf-8

import bcrypt

from db.sa import Session
from apps.blog import models


def init_user():
    session = Session()
    user = models.User(
        user_id=1,
        username='admin',
        password=str(
            bcrypt.hashpw('admin'.encode('utf-8'), bcrypt.gensalt()),
            'utf-8'
        ),
        avatar='http://img.l.jifangcheng.com/Katarina.png',
        introduction='hello',
    )
    session.add(user)
    session.commit()
    session.close()


def init_article():
    session = Session()
    article = models.Article(
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
