#!/usr/bin/env python
# coding=utf-8


from fabric.api import (
    local,
)


def runserver(_type='normal'):
    cmd = 'docker-compose run --rm -p 8004:8004 web '
    if _type == 'normal':
        cmd += 'python app.py'
    local(cmd)


def command(cmd):
    local(
        'docker-compose run --rm -p 8004:8004 web {}'.format(cmd)
    )


def test():
    local(
        'docker-compose run -e TESTING=True --rm web '
        'coverage run tests/runtests.py'
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


def update_packages():
    local('docker exec -it diana_web_run_1 pip install -r requirements.txt')
    local(
        'docker commit -m "update" -a "iawia002" diana_web_run_1 '
        'diana_web:latest'
    )


def init():
    local(
        'docker-compose run --rm web python db/init.py'
    )


def watch():
    local(
        'nodemon -x "python app.py -debug=True" -w static/dist'
    )
