#!/usr/bin/env python
# coding=utf-8

import unittest

import bcrypt

from test.base import BaseTest

from apps.blog.models import (
    Tag,
    User,
    Article,
)
from utils import tags


class BlogTest(BaseTest):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        session = cls.Session()
        cls.username = 'L'
        cls.password = 'L'
        user = User(
            username=cls.username,
            password=str(
                bcrypt.hashpw(cls.password.encode('utf-8'), bcrypt.gensalt()),
                'utf-8'
            ),
            avatar='Katarina.png',
            introduction='L'
        )
        article = Article(
            user=user,
            title='L',
            introduction='L',
            markdown_content='L',
            compiled_content='L',
        )
        tag = Tag(content='hello')
        article.tag.append(tag)
        user.tag.append(tag)
        session.add(user)
        session.add(article)
        session.commit()
        session.close()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('L', str(response.data))

    def test_article(self):
        response = self.client.get('/p/1')
        self.assertEqual(response.status_code, 200)

    def test_404(self):
        response = self.client.get('/1')
        self.assertEqual(response.status_code, 404)

    def test_statistics(self):
        with self.client:
            self.login(self.username, self.password)
            response = self.client.get('/statistics')
            self.assertEqual(response.status_code, 200)

    def test_more_index(self):
        response = self.client.get('/more', data={
            'next_page': 2,
            'page': 'index',
            'tag': ''
        })
        self.assertEqual(response.status_code, 200)

    def test_more_tag(self):
        response = self.client.get('/more', data={
            'next_page': 2,
            'page': 'tag',
            'tag': 'hello'
        })
        self.assertEqual(response.status_code, 200)

    def test_edit_get_new(self):
        with self.client:
            self.login(self.username, self.password)
            response = self.client.get('/p/0/edit')
            self.assertEqual(response.status_code, 200)

    def test_edit_get(self):
        with self.client:
            self.login(self.username, self.password)
            response = self.client.get('/p/1/edit')
            self.assertEqual(response.status_code, 200)
            self.assertIn('L', str(response.data))

    def test_edit_new(self):
        with self.client:
            self.login(self.username, self.password)
            response = self.client.post(
                '/p/0/edit',
                data={
                    'title': 'hello',
                    'introduction': 'hello',
                    'markdown_content': 'hello',
                    'compiled_content': 'hello',
                    'tags[]': ["hello", "tag"],
                },
            )
            self.assertEqual(response.status_code, 200)

    def test_edit(self):
        with self.client:
            self.login(self.username, self.password)
            response = self.client.post(
                '/p/1/edit',
                data={
                    'title': 'hello L',
                    'introduction': 'hello L',
                    'markdown_content': 'hello L',
                    'compiled_content': 'hello L',
                    'tags[]': ["hello"],
                },
            )
            self.assertEqual(response.status_code, 200)

    def test_tag(self):
        tag = tags.tag_url_encode('hello')
        response = self.client.get('/tag/%s' % tag)
        self.assertEqual(response.status_code, 200)
        self.assertIn('hello', str(response.data))

    def test_tags(self):
        response = self.client.get('/tags')
        self.assertEqual(response.status_code, 200)
        self.assertIn('hello', str(response.data))


if __name__ == '__main__':
    unittest.main()
