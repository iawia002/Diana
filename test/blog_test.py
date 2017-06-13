#!/usr/bin/env python
# coding=utf-8

import base64
import urllib
import unittest

import mock

import tornado.web
from test.base import BaseTest

from apps.blog.models import (
    Tag,
    User,
    Article,
)


class BlogTest(BaseTest):

    @classmethod
    def setUpClass(cls):
        super(BlogTest, cls).setUpClass()
        session = cls.Session()
        user = User(
            username='L',
            password='L',
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
        response = self.fetch('/')
        self.assertEqual(response.code, 200)
        self.assertIn('L', response.body)

    def test_article(self):
        response = self.fetch('/p/1')
        self.assertEqual(response.code, 200)

    def test_404(self):
        response = self.fetch('/1')
        self.assertEqual(response.code, 404)

    def test_more_index(self):
        base_url = '/more'
        params = {
            'next_page': 2,
            'page': 'index',
            'tag': ''
        }
        url = base_url + '?' + urllib.urlencode(params)
        response = self.fetch(url)
        self.assertEqual(response.code, 200)

    def test_more_tag(self):
        base_url = '/more'
        params = {
            'next_page': 2,
            'page': 'tag',
            'tag': 'hello'
        }
        url = base_url + '?' + urllib.urlencode(params)
        response = self.fetch(url)
        self.assertEqual(response.code, 200)

    @mock.patch.object(tornado.web.RequestHandler, 'get_secure_cookie')
    def test_edit_get_new(self, mock_login):
        mock_login.return_value = 1
        response = self.fetch('/p/0/edit')
        self.assertEqual(response.code, 200)

    @mock.patch.object(tornado.web.RequestHandler, 'get_secure_cookie')
    def test_edit_get(self, mock_login):
        mock_login.return_value = 1
        response = self.fetch('/p/1/edit')
        self.assertEqual(response.code, 200)
        self.assertIn('L', response.body)

    @mock.patch.object(tornado.web.RequestHandler, 'get_secure_cookie')
    def test_edit_new(self, mock_login):
        mock_login.return_value = 1
        response = self.fetch(
            '/p/0/edit',
            method='POST',
            body=urllib.urlencode({
                'title': 'hello',
                'introduction': 'hello',
                'markdown_content': 'hello',
                'compiled_content': 'hello',
                'tags[]': ["hello", "tag"],
            }, True)
        )
        self.assertEqual(response.code, 200)

    @mock.patch.object(tornado.web.RequestHandler, 'get_secure_cookie')
    def test_edit(self, mock_login):
        mock_login.return_value = 1
        response = self.fetch(
            '/p/1/edit',
            method='POST',
            body=urllib.urlencode({
                'title': 'hello L',
                'introduction': 'hello L',
                'markdown_content': 'hello L',
                'compiled_content': 'hello L',
                'tags[]': ["hello"],
            }, True)
        )
        self.assertEqual(response.code, 200)

    def test_tag(self):
        tag = base64.urlsafe_b64encode('hello'.encode('utf-8'))
        response = self.fetch('/tag/%s' % tag)
        self.assertEqual(response.code, 200)
        self.assertIn('hello', response.body)

    def test_tags(self):
        response = self.fetch('/tags')
        self.assertEqual(response.code, 200)
        self.assertIn('hello', response.body)


if __name__ == '__main__':
    unittest.main()
