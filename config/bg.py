#!/usr/bin/env python
# coding=utf-8

INDEX_BG = [
    {
        'url': 'http://img.l.jifangcheng.com/de0bd5aa1c181bfce7a08bd222f7d8681446204f.jpg',  # noqa
        'name': '前线指挥官 卡特琳娜',
        'quote': '以敌人之血，祭我大诺克萨斯',
    },
    {
        'url': 'http://img.l.jifangcheng.com/Katarina_9.jpg',
        'name': '',
        'quote': '源计划：雄心 卡特琳娜',
    },
    {
        'url': 'http://img.l.jifangcheng.com/6994b45384670c05b9c3467f89e9fb91ab5860d5.jpg',  # noqa
        'name': '铁血女忍 阿卡丽',
        'quote': '荣耀剑下取，均衡乱中求',
    },
    {
        'url': 'http://img.l.jifangcheng.com/01d58bbaa8c21b8ecfbd17068852a8b0aae28abb.jpg',  # noqa
        'name': '诺克萨斯统领 斯维因 Swain',
        'quote': '在我手中，诺克萨斯必将再度崛起',
    },
    {
        'url': 'http://img.l.jifangcheng.com/Ashe_8.jpg',
        'name': '源计划：联合 艾希',
        'quote': '只有能被明日的我们铭记，今天才有意义',
    },
    {
        'url': 'http://img.l.jifangcheng.com/95359b84a58b384688030ad2002b48df551f967c.jpg',  # noqa
        'name': '皎月女神 黛安娜 Diana',
        'quote': '他们让我别无选择',
    },
    {
        'url': 'http://img.l.jifangcheng.com/35cde892b621978d8b2fec069d70223f165e2e1b.jpg',  # noqa
        'name': '暗黑女武神 黛安娜',
        'quote': '拥抱黑暗吧',
    },
    {
        'url': 'http://img.l.jifangcheng.com/8d795cfc27f8cfc91b71db704ea4a00e290becd1.jpg',  # noqa
        'name': '刺客信条 锐雯',
        'quote': '我已经流浪了如此之久',
    },
    {
        'url': 'http://img.l.jifangcheng.com/56b2aae5bbad252bad017c3d83d2091657439fa4.jpg',  # noqa
        'name': '冠军之刃 锐雯',
        'quote': '断剑重铸之日，骑士归来之时',
    },
    {
        'url': 'http://img.l.jifangcheng.com/db26fe7e0a38787fb1349068b9f49c34c8e504ae.jpg',  # noqa
        'name': '',
        'quote': 'ANNIE: Origins',
    },
    {
        'url': 'http://img.l.jifangcheng.com/ee8a9ab96f2cca9380f5ac1a96e982dcfdc6be31.jpg',  # noqa
        'name': '虚空之女 卡莎 Kaisa',
        'quote': '我回来，是为了那些回不来的人',
    },
    {
        'url': 'http://img.l.jifangcheng.com/8641b730ac1a67fdf610cef2b3d1c1ed855675aa.jpg',  # noqa
        'name': '刀锋舞者 艾瑞莉娅 Irelia',
        'quote': '让他们来吧，这片土地将是他们的坟墓',
    },
    {
        'url': 'http://img.l.jifangcheng.com/ad6df7e18d807719ba9066b9206f46b79291fb64.jpg',  # noqa
        'name': '暗裔剑魔 亚托克斯 Aatrox',
        'quote': '我曾经有另一个名字',
    },
    {
        'url': 'http://img.l.jifangcheng.com/574bed55a9df38ae959cddec5ac12f158dfdf8c8.jpg',  # noqa
        'name': '腥红之月 烬',
        'quote': '我于杀戮之中盛放，亦如黎明中的花朵',
    },
    {
        'url': 'http://img.l.jifangcheng.com/1fb91f1bf6680a2f28adc4e640a0483d3a3431eb.jpg',  # noqa
        'name': '死兆星 锤石',
        'quote': '你自身难保，还怎么保护整个世界',
    },
    {
        'url': 'http://img.l.jifangcheng.com/c355e40edd4fbb29f72a032720f859912e00e736.jpg',  # noqa
        'name': '影流之镰 凯隐 Kayn',
        'quote': '你把我教的太好了，师傅',
    },
    {
        'url': 'http://img.l.jifangcheng.com/93bcb7a6039c7a06d9ed5720f8a6ac300048d435.jpg',  # noqa
        'name': '瓦洛兰之盾 塔里克 Taric',
        'quote': '我曾踏足山巅，也曾进入低谷',
    },
    {
        'url': 'http://img.l.jifangcheng.com/947dfdc544b3feab03767210486c266a0ca69d9d.jpg',  # noqa
        'name': '腥红之月 卡莉丝塔',
        'quote': '所有背叛者，都得死',
    },
    {
        'url': 'http://img.l.jifangcheng.com/7bb5317d17a1e32622622fc3db006141fadbe868.jpg',  # noqa
        'name': '大元素使 拉克丝',
        'quote': '并非是我选择了黑暗，是黑暗选择了我',
    },
    {
        'url': 'http://img.l.jifangcheng.com/a434ada81e41792400b6c8f12d4592b2d679995f.jpg',  # noqa
        'name': '丧尸杀手 金克丝',
        'quote': '我是个疯子，有医生开的证明',
    },
    {
        'url': 'http://img.l.jifangcheng.com/d3e02d1ba8594636c798f543808cb8ef1d77101a.jpg',  # noqa
        'name': '疾风剑豪 亚索 Yasuo',
        'quote': '落叶的一生，只是为了归根吧',
    },
    {
        'url': 'http://img.l.jifangcheng.com/5d677868a5b6d3713ceb7381c540dfdf1d3c2979.jpg',  # noqa
        'name': '永猎双子 千珏 Kindred',
        'quote': '执子之魂，与子共生',
    },
    {
        'url': 'http://img.l.jifangcheng.com/73260db60245e74c21afc00b87ca4a9cd2cd9ed8.jpg',  # noqa
        'name': '沙漠皇帝 阿兹尔 Azir',
        'quote': '恕瑞玛，你的皇帝回来了',
    },
    {
        'url': 'http://img.l.jifangcheng.com/926dbe6553fe4dbe23c00274e418858f088040a4.png',  # noqa
        'name': '狐妖小红娘',
        'quote': '让他们来许愿吧',
    },
    {
        'url': 'http://img.l.jifangcheng.com/15de04a1863c22e4b531e687cbb66504af20e29b.png',  # noqa
        'name': '宝石之国',
        'quote': '那个冬天，老师失去了两个孩子',
    },
    {
        'url': 'http://img.l.jifangcheng.com/68ae837e8306c7a75261ebd18d8b2c352aec2442.png',  # noqa
        'name': '宝石之国',
        'quote': '以我所有，换我所无',
    },
    {
        'url': 'http://img.l.jifangcheng.com/66ef87e7d53fdae618fccafcce339387c36f9a7d.png',  # noqa
        'name': '少女终末旅行',
        'quote': '能吃的东西，就能吃',
    },
]
