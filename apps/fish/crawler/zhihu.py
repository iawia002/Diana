# coding=utf-8

import time
import logging

import requests
from bs4 import BeautifulSoup

import config
import utils.db
from app import celery
from db.sa import Session
from apps.fish.models import (
    Record,
    UpdateInfo
)


'''
<div class="zm-editable-content clearfix">
    <img
        src="//zhstatic.zhihu.com/assets/zhihu/ztext/whitedot.jpg"
        data-rawwidth="746"
        data-rawheight="823"
        class="origin_image zh-lightbox-thumb lazy"
        width="746"
        data-original="https://pic3.zhimg.com/v2-150ecb41e823c5f650058ab181ce1286_r.png"
        data-actualsrc="https://pic3.zhimg.com/v2-150ecb41e823c5f650058ab181ce1286_b.png"
    >
</div>
'''


def img_with_data_original(tag):
    if tag.name == 'img' and tag.has_attr('data-original') \
            and set(['origin_image', 'lazy']).issubset(set(tag['class'])):
        return tag


def imgs(url):
    include = 'data[*].is_normal,is_sticky,collapsed_by,suggest_edit,comment_count,collapsed_counts,reviewing_comments_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,mark_infos,created_time,updated_time,relationship.is_author,voting,is_thanked,is_nothelp,upvoted_followees;data[*].author.is_blocking,is_blocked,is_followed,voteup_count,message_thread_token,badge[?(type=best_answerer)].topics'  # noqa
    limit = 20
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/601.7.8',  # noqa
        'Host': 'www.zhihu.com',
        'Cookie': config.ZH_COOKIE,
    }
    ZH_API = (
        'https://www.zhihu.com/api/v4/questions/{question_id}/answers?'
        'include={include}&sort_by=default&limit={limit}&offset={offset}'
    ).format

    url = url.split('?')[0]
    if url[-1] == '/':
        question_id = url.split('/')[-2]
    else:
        question_id = url.split('/')[-1]
    html_text = requests.get(
        url,
        headers=headers,
    ).text
    soup = BeautifulSoup(html_text, 'html.parser')
    title = soup.title.string
    brackets = title.find(')')  # 处理标题前缀是 (30 条消息) 这种情况
    if title[0] == '(' and brackets != -1:
        title = title[brackets+1:]

    answer_url = ZH_API(
        include=include,
        question_id=question_id,
        limit=1,
        offset=0,
    )
    r = requests.get(answer_url, headers=headers)
    answer_num = r.json()['paging']['totals']

    page = answer_num / limit
    if answer_num % limit != 0:
        page += 1
    answers = []

    time.sleep(2)  # 睡眠 2 s，知乎有反爬虫策略
    for item in xrange(page):
        answer_url = ZH_API(
            include=include,
            limit=limit,
            question_id=question_id,
            offset=item*limit
        )
        r = requests.get(answer_url, headers=headers)
        data = r.json()['data']
        answers.extend([item['content'] for item in data])

        time.sleep(2)  # 睡眠 2 s，知乎有反爬虫策略
    img_list = []
    for answer in answers:
        soup = BeautifulSoup(answer, 'html.parser')
        imgs = soup.find_all(img_with_data_original)
        img_list.extend([img['data-original'] for img in imgs])
    return {'title': title, 'images': img_list}


@celery.task(name='jike')
def jike():
    '''
    即刻：知乎热门钓鱼帖
    '''
    JK_API = (
        'https://app.jike.ruguoapp.com/1.0/messages/showDetail?'
        'topicId={topic_id}'
    ).format(topic_id='57281cf75f0ba71200ffde92')
    results = requests.get(
        JK_API,
    )
    if results.status_code != 200:
        logging.error(
            '[fish] jike api url failed, status_code: {}'.format(
                results.status_code
            )
        )
        return
    results = results.json()
    messages = results['messages']
    messages_url = [message['linkUrl'] for message in messages]
    session = Session()
    update_record = session.query(UpdateInfo).first()
    already_existing = update_record.content
    # 用这次的 URL 列表减去已经存在的 URL 列表，得到这次多出来的 URL
    need_update = list(set(messages_url) - set(already_existing))
    for url in need_update:
        article = utils.db.get_instance(session, Record, source=url)
        result = imgs(url)
        article.content = result['images']
        article.title = result['title']
        article.image_num = len(result['images'])
        session.add(article)
    total = []
    total.extend(already_existing)
    total.extend(need_update)
    update_record.content = total
    session.add(update_record)
    session.commit()
    session.close()
    return need_update


def update_manually(url):
    session = Session()

    # 更新文章
    article = utils.db.get_instance(session, Record, source=url)
    result = imgs(url)
    article.content = result['images']
    article.title = result['title']
    article.image_num = len(result['images'])

    # 更新记录
    update_record = session.query(UpdateInfo).first()
    total = []
    total.extend(update_record.content)
    if url not in total:
        total.append(url)
    update_record.content = total

    session.add(article)
    session.add(update_record)
    try:
        session.commit()
    except:
        session.rollback()
        raise
    session.close()


def batch_update(urls):
    for url in urls:
        update_manually(url)


if __name__ == '__main__':
    __import__('ipdb').set_trace()
