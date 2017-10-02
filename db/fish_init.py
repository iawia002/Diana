# coding=utf-8

from db.sa import Session
from apps.fish.models import UpdateInfo


def init_update_record():
    session = Session()
    update_record = UpdateInfo(update_id=1, content=[])
    session.add(update_record)
    session.commit()
    session.close()


if __name__ == '__main__':
    init_update_record()
