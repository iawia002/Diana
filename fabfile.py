#!/usr/bin/env python
# coding=utf-8


from fabric.api import (
    local,
)


def runserver():
    local(
        'docker-compose run --rm -p 8004:8004 web python app.py'
    )


def command(cmd):
    local(
        'docker-compose run --rm -p 8004:8004 web {}'.format(cmd)
    )


def test():
    local(
        'docker-compose run -e TESTING=True --rm web '
        'coverage run test/runtests.py'
    )


def makemigrations(msg=''):
    local(
        'docker-compose run --rm web alembic revision '
        '--autogenerate -m "{}"'.format(msg)
    )


def migrate(env='docker'):
    if env == 'local':
        local(
            'alembic upgrade head'
        )
    else:
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


def init(env='docker'):
    if env == 'local':
        local(
            'python db/init.py'
        )
    else:
        local(
            'docker-compose run --rm web python db/init.py'
        )


def watch():
    local(
        'nodemon -x "python app.py -debug=True" -w static/dist'
    )
