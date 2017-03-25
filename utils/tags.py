#!/usr/bin/env python
# coding=utf-8

import base64

import pinyin


def tag_url_encode(name):
    '''
    base64 不能对 unicode 进行操作，所以要先转换成 byte
    '''
    return base64.urlsafe_b64encode(name.encode('utf-8'))


def tag_url_decode(name):
    try:
        name = base64.urlsafe_b64decode(str(name)).decode('utf-8')
    except Exception:
        return None
    return name


def single_get_first(string):
    '''
    获取中文拼音的首字母
    '''
    return pinyin.get_initial(string).upper()


if __name__ == '__main__':
    print single_get_first('皎')
