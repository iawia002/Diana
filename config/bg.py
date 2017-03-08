#!/usr/bin/env python
# coding=utf-8

INDEX_BG = [
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Katarina_5.jpg',
        'name': '前线指挥官 卡特琳娜'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Katarina_0.jpg',
        'name': '不祥之刃 卡特琳娜'
    },
    {
        'url': 'http://img.l.jifangcheng.com/Katarina_9.jpg',
        'name': '源计划：雄心 卡特琳娜'
    },
    {
        'url': 'http://img.l.jifangcheng.com/Ashe_8.jpg',
        'name': '源计划：联合 艾希'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Akali_4.jpg',
        'name': '实习护士 阿卡丽'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Akali_2.jpg',
        'name': '绯红 阿卡丽'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Irelia_1.jpg',
        'name': '夜刃 艾瑞莉娅'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Ahri_4.jpg',
        'name': '偶像歌手 阿狸'
    },
    {
        'url': 'http://img.l.jifangcheng.com/d3860d14623dcdb45f51220b19fc8408d3461eab.jpg',  # noqa
        'name': '勇者 阿狸'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Annie_6.jpg',
        'name': '安伯斯与提妮'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Diana_0.jpg',
        'name': '皎月女神 黛安娜'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Diana_1.jpg',
        'name': '暗黑女武神 黛安娜'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Fiora_4.jpg',
        'name': '源计划：火 菲奥娜'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Lucian_6.jpg',
        'name': '源计划：雷 卢锡安'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Shyvana_4.jpg',
        'name': '冰霜亚龙 希瓦娜'
    },

    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Sivir_7.jpg',
        'name': '光明骑士 希维尔'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Ashe_7.jpg',
        'name': '黑暗骑士 艾希'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Sivir_8.jpg',
        'name': '胜利女神 希维尔'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Morgana_6.jpg',
        'name': '胜利女神 莫甘娜'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Soraka_4.jpg',
        'name': '灵魂收割者 索拉卡'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Sion_5.jpg',
        'name': '霸天零式 赛恩'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Evelynn_4.jpg',
        'name': '惊天魔盗 伊芙琳'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Riven_1.jpg',
        'name': '刺客信条 锐雯'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Ezreal_7.jpg',
        'name': '光执事 伊泽瑞尔'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Yasuo_1.jpg',
        'name': '西部牛仔 亚索'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Riven_4.jpg',
        'name': '冠军之刃 锐雯'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Ezreal_8.jpg',
        'name': '黑桃皇牌 伊泽瑞尔'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Zed_3.jpg',
        'name': '源计划：阴 劫'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Ezreal_3.jpg',
        'name': '冰川勇者 伊泽瑞尔'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Pantheon_6.jpg',
        'name': '屠龙勇士 潘森'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/AurelionSol_0.jpg',
        'name': '铸星龙王 奥瑞利安·索尔'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Kalista_1.jpg',
        'name': '腥红之月 卡莉丝塔'
    },
    {
        'url': 'http://7xqk8o.com1.z0.glb.clouddn.com/Lulu_3.jpg',
        'name': '驯龙女巫 璐璐'
    },
    {
        'url': 'http://img.l.jifangcheng.com/o_1a7rcga441ldd7fb1fb8mb4q2a.jpg',
        'name': '电玩系列'
    },
    {
        'url': 'http://img.l.jifangcheng.com/Sona_2.jpg',
        'name': '五杀摇滚键盘手 娑娜'
    },
    {
        'url': 'http://img.l.jifangcheng.com/Sivir_5.jpg',
        'name': '创战纪 希维尔'
    },
    {
        'url': 'http://img.l.jifangcheng.com/Azir_3.jpg',
        'name': 'SKT T1 冠军皮肤'
    },
    {
        'url': 'http://img.l.jifangcheng.com/Zed_10.jpg',
        'name': '冠军之隐 劫'
    },
    {
        'url': 'http://img.l.jifangcheng.com/54afcf81358f9c508ad11f9b09f20eaa1ec712b7.jpg',  # noqa
        'name': '游侠法师 拉克丝'
    },
    {
        'url': 'http://img.l.jifangcheng.com/7bb5317d17a1e32622622fc3db006141fadbe868.jpg',  # noqa
        'name': '大元素使 拉克丝'
    },
]

INDEX_SAYING = [
    '我一路向北，离开有你的季节',
    "We don't talk anymore",
]
