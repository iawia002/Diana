#!/usr/bin/env python
# coding=utf-8


from fabric.api import (
    local,
)


def dev():
    local(
        'docker-compose run -e FLASK_ENV=development --rm '
        '-p 8004:8004 web python app.py'
    )


def command(cmd):
    local(
        'docker-compose run --rm -p 8004:8004 web {}'.format(cmd)
    )


def test():
    local(
        'docker-compose run -e TESTING=True --rm web '
        'coverage run tests/runtests.py'
    )


def test_func(func):
    local(
        'docker-compose run -e TESTING=True --rm web '
        'python tests/blog_test.py BlogTest.{}'.format(func)
    )


def celery_worker():
    local(
        'docker-compose run --rm web '
        'celery -A main.celery worker --autoscale=10,1 -l INFO'
    )


def celery_beat():
    local(
        'docker-compose run --rm web '
        'celery -A main.celery beat -l INFO'
    )


def makemigrations(msg=''):
    local(
        'docker-compose run --rm web alembic revision '
        '--autogenerate -m "{}"'.format(msg)
    )


def migrate():
    local(
        'docker-compose run --rm web alembic upgrade head'
    )


def alembic(command='current'):
    '''
    alembic upgrade +2
    alembic downgrade -1
    '''
    local(
        'docker-compose run --rm web alembic {}'.format(command)
    )


def shell():
    local(
        'docker-compose run --rm web ipython'
    )


def upgrade_packages():
    '''更新依赖
    '''
    local('docker build -t iawia002/diana:latest -f ./Dockerfile .')
    local('docker push iawia002/diana:latest')


def init():
    local(
        'docker-compose run --rm web python db/init.py'
    )


def watch():
    local(
        'nodemon -x "python app.py -debug=True" -w static/dist'
    )
