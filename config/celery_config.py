# coding=utf-8

import config


if config.REDIS_PASSWORD:
    result_backend = 'redis://:{password}@{host_port}/{db}'.format(
        password=config.REDIS_PASSWORD,
        host_port=config.REDIS_HOST_PORT,
        db=config.REDIS_DB + 1,
    )
    broker_url = 'redis://:{password}@{host_port}/{db}'.format(
        password=config.REDIS_PASSWORD,
        host_port=config.REDIS_HOST_PORT,
        db=config.REDIS_DB + 2,
    )
else:
    result_backend = 'redis://{host_port}/{db}'.format(
        host_port=config.REDIS_HOST_PORT,
        db=config.REDIS_DB + 1,
    )
    broker_url = 'redis://{host_port}/{db}'.format(
        host_port=config.REDIS_HOST_PORT,
        db=config.REDIS_DB + 2,
    )

timezone = 'Asia/Shanghai'

imports = (
    'apps.fish.crawler.zhihu',
)

result_expires = 24 * 60 * 60  # One day

beat_schedule = {
    # 即刻，知乎热门钓鱼贴
    'jike': {
        'task': 'jike',
        'schedule': 10 * 60,
    },
}
