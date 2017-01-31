#!/usr/bin/env python
# coding=utf-8

from tornado.testing import main
from tornado.test.util import unittest


TEST_MODULES = [
    'test.blog_test',
]


def all():
    return unittest.defaultTestLoader.loadTestsFromNames(TEST_MODULES)

if __name__ == '__main__':
    main()
