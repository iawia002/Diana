#!/usr/bin/env python
# coding=utf-8

import unittest

import bcrypt

from tests.base import BaseTest

from utils import tags
from apps.blog.models import (
    Tag,
    Article,
)
from apps.auth.models import User
from apps.fish.models import Record


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

        fish_record = Record(
            title='hello',
            content=['hello'],
            image_num=1,
            source='hello',
        )
        session.add(fish_record)
        session.commit()
        session.close()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('L', str(response.data))

    def test_article(self):
        response = self.client.get('/p/1')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/p/100')
        self.assertEqual(response.status_code, 404)

    def test_404(self):
        response = self.client.get('/1')
        self.assertEqual(response.status_code, 404)

    def test_statistics(self):
        with self.client:
            self.login(self.username, self.password)
            response = self.client.get('/statistics')
            self.assertEqual(response.status_code, 200)

    def test_login_post(self):
        response = self.client.post(
            '/auth/login',
            json={
                'username': 'L',
                'password': 'L',
            },
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            '/auth/login',
            json={
                'username': 'L',
                'password': 'hello',
            },
        )
        self.assertEqual(response.status_code, 400)

    def test_logout(self):
        response = self.client.get('/auth/logout')
        self.assertEqual(response.status_code, 302)

    def test_more_index(self):
        for page in range(1, 3):
            response = self.client.get('/more', query_string={
                'next_page': page,
                'page': 'index',
                'tag': ''
            })
            self.assertEqual(response.status_code, 200)

    def test_more_tag(self):
        for page in range(1, 3):
            response = self.client.get('/more', query_string={
                'next_page': page,
                'page': 'tag',
                'tag': 'hello'
            })
            self.assertEqual(response.status_code, 200)

    def test_unauthorized_edit(self):
        self.logout()
        response = self.client.get('/p/0/edit')
        self.assertEqual(response.status_code, 302)

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
                json={
                    'title': 'hello',
                    'introduction': 'hello',
                    'markdown_content': 'hello',
                    'compiled_content': 'hello',
                    'tags': ["hello", "tag"],
                },
            )
            self.assertEqual(response.status_code, 200)

    def test_edit(self):
        with self.client:
            self.login(self.username, self.password)
            response = self.client.post(
                '/p/1/edit',
                json={
                    'title': 'hello L',
                    'introduction': 'hello L',
                    'markdown_content': 'hello L',
                    'compiled_content': 'hello L',
                    'tags': ["hello"],
                },
            )
            self.assertEqual(response.status_code, 200)

    def test_tag(self):
        tag = tags.tag_url_encode('hello')
        response = self.client.get('/tag/{}'.format(tag))
        self.assertEqual(response.status_code, 200)
        self.assertIn('hello', str(response.data))

        response = self.client.get('/tag/aa')
        self.assertEqual(response.status_code, 404)

    def test_tags(self):
        response = self.client.get('/tags')
        self.assertEqual(response.status_code, 200)
        self.assertIn('hello', str(response.data))

    def test_user_api(self):
        with self.client:
            self.login(self.username, self.password)
            response = self.client.post(
                '/user',
                json={
                    'introduction': 'hello L',
                },
            )
            self.assertEqual(response.status_code, 200)

            response = self.client.post('/user', json={})
            self.assertEqual(response.status_code, 400)

    def test_fish(self):
        response = self.client.get('/fish')
        self.assertEqual(response.status_code, 200)

    def test_fish_article(self):
        response = self.client.get('/fish/p/1')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/fish/p/100')
        self.assertEqual(response.status_code, 404)

    def test_fish_more(self):
        response = self.client.get('/fish/more', query_string={
            'next_page': 'a',
        })
        self.assertEqual(response.status_code, 400)

        for page in range(1, 3):
            response = self.client.get('/fish/more', query_string={
                'next_page': page,
            })
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
