# -*- coding: utf-8 -*-
import re
from aip import AipNlp
CURRENT_RULE = None

APP_ID =*
API_KEY =*
SECRET_KEY =*
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
# 规则提取关系

# 合并title
# TODO 这里最好传入pos_sent,然后对一些连续标记为ti的进行处理
def processBeforeRule(pos_sent):
    # TODO 亟待预处理36kr前文中的编者话，建议放置在html解析部分
    # TODO 36kr的每日速递或者8点1氪需要单独处理

    # TODO 微信公众号的拓展阅读


    pass


# TODO rule1和rule2中nz和nt合并的问题

# 为了加速编译
rules = [
    # rule1
    [
        re.compile(
            r'(?:/\w{1,3} )?([^ /][\w ()（）\.-]{1,})/nt(?: \(.*\)/w)?(?:  /w)?(?: ?([^ /]{2,})/ti)?(?:  /w)?(?: ?([^ ][\w ]{1,})/nr)')
    ],
    # rule2
    [
        re.compile(r'(?:/\w{1,3} )?(?: ?([\w()（） \.-]{1,})/(?:n[szt]))(?:  /w)*?(?: ?([\w &]{2,})/ti)(?:  /w)?(?: ?([^ ][\w ]{1,})/nr)')
    ],
    # rule3
    [
        re.compile(
            r'(?:/\w{1,3} )?(?: ?([^ /][\w ()（）\.-]{1,})/nt)(?: ?(\w{2,})/ti) (?:(?:[兼和]/[cv])|(?:及/c)|(?:&/w))(?:  /w)?(?:([^。，！,.!]{1,30}?)/ti)(?:  /w)?(?: ?([^ ][\w ]{1,})/nr)')
    ],
    # rule4
    [
        re.compile(
            r'(?:(?:/\w{1,3} )?([^ /][\w ()（）\.-]{1,})/nt(?: [(（].*[）)]/w)?([^、，]*(?:\w{2,}))/ti) (?:(?:[兼和]/[cv])|(?:及/c)|(?:[&、]/w)) ([^ /][\w ()（）\.-]{1,})/nt(?: [(（].*[）)]/w)?([^、，/]*(?:\w{2,}))/ti(?:  /w)? (?: ?([^ ][\w ]{1,})/nr)')
    ],
    # rule5
    [
        re.compile(
            r'(?:/\w{1,3} )?(?:([^ /][\w ()（）\.-]{1,})/nt)((?:(?:(?: ./w))?(?: (?:\w{2,})/ti))+)(?: ([^ ][\w ]{1,})/nr)'),
        re.compile('(\w{2,})/ti')
    ],
    # rule6
    [
        re.compile(r'(?:/\w{1,3} )?([^ /][\w （）()\.-]{1,})/nt 的/u(?: (\w{2,})/ti)? ([^ ][\w ]{1,})/nr')
    ],
    # rule7
    [
        re.compile(r'(?:/\w{1,3} )?([^ ][\w ]{1,})/nr'),
        re.compile(r'(?:/\w{1,3} )?([^ ][\w ]{1,})/nr(?![^ ][\w ]{1,}/nr).* ([^ /][\w ()（）\.-]{1,})/(?:nt)(?: 的/u)? (\w{2,})/ti'),
        re.compile(
            r'(?:/\w{1,3} )?([^ ][\w ]{1,})/nr.* (?:(?:[前|原]/\w{1,3})|(?:曾/\w{1,3} [任|是]/\w{1,3})) ([^ /][\w ()（）\.-]{1,})/(?:(?:nt)|(?:nz))(?: 的/u)? (\w{2,})/ti'),

        re.compile(
            r'(?:/\w{1,3} )?([^ ][\w ]{1,})/nr((?:.*/w(?:(?: [^ /][\w ]{1,}/(?:(?:n[tz]?)|(?:vn)))+) \w{2,}/ti)+)'),
        re.compile(r'((?: \w+/(?:(?:n[tz]?)|(?:vn)))+) (\w{2,})/ti'),
        re.compile(r'([^ ][\w ]{1,})/(?:(?:n[tz]?)|(?:vn))'),

        re.compile(
            r'(?<!/v )(?:/\w{1,3} )?(?:([^ ][\w ]{1,})/nr)((?:(?:(?: [^、()（）！!]/w)?(?: [^ /][\w ()（）\.-]{1,}/nt)(?: \w{2,}/ti)?)|(?:(?: ./w)?(?: \w{2,}/(?:(?:ns)|(?:nz))(?: \w{2,}/ti))))+)'),
        re.compile(
            '(?:(?: ./w)?(?: ?([^ /][\w ()（）\.-]{1,})/nt)(?: ?(\w{2,})/ti)?)|(?:(?:(?: ./w)(?: (\w{2,})/(?:(?:ns)|(?:nz))(?: (\w{2,})/ti))))'),

        re.compile(
            r'(?:/\w{1,3} )?(?: ?([^ ][\w ]{1,})/nr) 是/v((?:(?: [^ /w]+/\w{1,3})+ (?:[^ /][\w ()（）\.-]{1,})/nt(?: [(（].*[）)]/w)?(?: 的/u)?(?:(?: [^ /w]+/\w{1,3})* (?:\w{2,})/ti))+)'),
        re.compile(r' ([^ /][\w ()（）\.-]{1,})/nt(?: [(（].*[）)]/w)?(?: 的/u)?([^、，]*(?:\w{2,}/ti))(?: [，、，]/w)?'),
        re.compile(r' ([ \w]*)/\w{1,3}')

    ],
    # rule8
    [
        re.compile(
            r'(?:/\w{1,3} )?(?: ?.+/w )?((?: ?[\w ()（）\.]{1,}/(?:(?:n[tsz]?)|(?:vn)) )+)(\w{2,})/ti ([^ ][\w ]{1,})/nr'),
        re.compile(r'(?:/\w{1,3} )?([\w ()（）]{1,})/(?:(?:n[tsz]?)|(?:vn))')
    ],
    # rule9
    [
        re.compile(
            r'(?:/\w{1,3} )?([^ /][\w ()（）\.-]{1,})/nt((?: \w+/(?:(?:n)|(?:vn)|(?:ti)))+)(?:  /w)? (?:(?:[兼和]/[cv])|(?:及/c)|(?:&/w))(?:  /w)? (\w{2,})/ti(?:  /w)? (\w{2,})/nr'),
        re.compile(r'(?:/\w{1,3} )?([^ /][\w ]{1,})/(?:(?:n)|(?:vn)|(?:ti))')
    ],
    # rule10
    [
        re.compile(
            r'(?:/\w{1,3} )?([^ /][\w ()（）\.-]{1,})/nt(?:  /w)? (\w{2,})/ti(?:  /w)? (?:(?:[兼和]/[cv])|(?:及/c)|(?:&/w))((?: \w+/(?:(?:n)|(?:vn)|(?:ti)))+)(?:  /w)? (\w{2,})/nr'),
        re.compile(r'(?:/\w{1,3} )?([^ /][\w ]{1,})/(?:(?:n)|(?:vn)|(?:ti))')
    ],
    # rule11
    [

    ]
]


# 处理异常包含\w等字符
def stripText(text):
    textlist = text.split('/')

    if len(textlist) != 1 or len(text) > 30:
        raise Exception(f'{CURRENT_RULE}解析{text}出错！')

    return text.strip()


def rule1(sent_pos):
    # 明略数据金融事业部/nt 解决方案专家/ti 杨昀/nr
    global CURRENT_RULE
    CURRENT_RULE = 'rule1'
    p = rules[0][0]

    # 权重(暂定义1到10)
    weight = 10

    rels = set()

    for r in p.findall(sent_pos):
        try:
            org = stripText(r[0])
            name = stripText(r[2])
            title = stripText(r[1])
            if not not org and not not name:
                rels.add((name, org, title))
        except Exception as e:
            pass
    return rels, weight


def rule2(sent_pos):
    # '英诺天使基金/nz 创始合伙人/ti  /w 李竹/nr'
    global CURRENT_RULE
    CURRENT_RULE = 'rule2'
    p = rules[1][0]

    weight = 10
    rels = set()

    for r in p.findall(sent_pos):
        try:
            org = stripText(r[0])
            name = stripText(r[2])
            title = stripText(r[1])

            if name and org:
                rels.add((name, org, title))
        except Exception as e:
            pass
    return rels, weight


# 用于识别rule1无法提取title的情况
def rule3(sent_pos):
    # 明略数据/nt 技术合伙人/ti 兼/v SCOPA/nz 产品经理/ti 任鑫琦/nr
    global CURRENT_RULE
    CURRENT_RULE = 'rule3'
    p = rules[2][0]
    weight = 9
    rels = set()

    for r in p.findall(sent_pos):
        try:
            org = stripText(r[0])
            name = stripText(r[3])
            title = stripText(r[1])

            if not org or not name:
                continue
            rels.add((name, org, title))

            title2 = ''.join([
                ps.split('/')[0].strip() for ps in r[2].split(' ')
            ])

            title2 = stripText(title2)

            if not not title2:
                rels.add((name, org, title2))
        except Exception as e:
            pass
    return rels, weight


def rule4(sent_pos):
    # '对此/d ，/w 58集团/nt 高级副总裁/ti 、/w 安居客/nt COO/ti 叶兵/nr 回应/v 称/v'
    global CURRENT_RULE
    CURRENT_RULE = 'rule4'
    p = rules[3][0]
    weight = 6

    rels = set()
    for r in p.findall(sent_pos):
        try:
            name = stripText(r[-1])
            if name:
                org1 = stripText(r[0])
                title1 = stripText(r[1])
                if org1:
                    rels.add((name, org1, title1))
                org2 = stripText(r[2])
                title2 = stripText(r[3])
                if org2:
                    rels.add((name, org2, title2))
        except Exception as e:
            pass
    return rels, weight


def rule5(sent_pos):
    # '中车株洲电力机车研究所有限公司/nt 副总经理/ti 、/w 总工程师/ti 冯江华/nr 则/c 对/p 未来/t 电池/n 的/u 发展/vn 做出/v 了/u 预估/vn 。/w'
    global CURRENT_RULE
    CURRENT_RULE = 'rule5'
    p1 = rules[4][0]
    p2 = rules[4][1]
    weight = 7
    rels = set()
    for r in p1.findall(sent_pos):
        try:
            name = stripText(r[2])
            org = stripText(r[0])
            if not name or not org:
                continue
            for t in p2.findall(r[1]):
                try:
                    title = stripText(t)
                    rels.add((name, org, title))
                except Exception as e:
                    pass
        except Exception as e:
            pass

    return rels, weight


def rule6(sent_pos):
    # '美团/nt 的/u 王兴/nr 、/w 搜狗/nt 的/u 王小川/nr 、/w 航班/n 管家/n 的/u 王江/nr 和/c 李黎军/nr 、/w 昆仑万维/nt 的/u 周亚辉/nr 、/w 柠檬微趣/nt 的/u 齐伟/nr 都是/v 。/w'
    global CURRENT_RULE
    CURRENT_RULE = 'rule6'
    p = rules[5][0]
    weight = 6
    rels = set()

    for r in p.findall(sent_pos):
        try:
            org = stripText(r[0])
            name = stripText(r[2])
            title = stripText(r[1])

            if name and org:
                rels.add((name, org, title))
        except Exception as e:
            pass
    return rels, weight


#   原，曾是，历任等trigger词匹配规则
def rule7(sent_pos):
    '''
    :param sent_pos: 标注的句子
    :return: 关系，set类型

    定义：一句话中只出现一个人名，且符合一定形式
    '''
    # '4/w Andy Grove/nr 是/v 一个/m 从/p 恐怖/a 统治/vn 中/f 逃离/v 的/u 匈牙利/ns 难民/n 。/w 他/r 学习/v 的/u 是/v 工程学/n ，/w 并/c 最终/ad 作为/v 英特尔/nt 的/u 首席执行官/ti 引领/v 了/u 个人电脑/n 革命/vn 。/w 他/r 与/p 帕金森病/nz 进行/v 了/u 长时间/n 的/u 斗争/vn ，/w 最终/ad 在/p 2016年/t 早些/t 时候/n ，/w 于/p 硅谷/ns 过世/v ，/w 享年/n 79岁/m 。/w'
    global CURRENT_RULE
    CURRENT_RULE = 'rule7'
    p1 = rules[6][0]
    weight = 4
    rels = set()

    names = set(p1.findall(sent_pos))

    if len(names) != 1:
        return rels, weight

    name = names.pop().strip()

    # 识别人-公司-title形式

    p2 = rules[6][1]
    for r in p2.findall(sent_pos):
        try:
            org = stripText(r[1])
            title = stripText(r[2])

            rels.add((name, org, title))

        except Exception as e:
            pass
    p3 = rules[6][2]
    for r in p3.findall(sent_pos):
        try:
            org = stripText(r[1])
            title = stripText(r[2])
            if not not org:
                rels.add((name, org, title))
        except Exception as e:
            pass

    # 识别：人名+标点+是+org+title类似功能
    p4 = rules[6][3]
    for r in p4.findall(sent_pos):
        p5 = rules[6][4]
        for r1 in p5.findall(r[1]):
            try:
                p6 = rules[6][5]
                title = stripText(r1[1])
                org = ''.join(p6.findall(r1[0]))
                org = stripText(org)
                if not not org:
                    rels.add((name, org, title))
            except Exception as e:
                pass

    p7 = rules[6][6]
    for r in p7.findall(sent_pos):
        try:
            name = stripText(r[0])
            p8 = rules[6][7]
            for t in p8.findall(r[1]):
                try:
                    org1 = stripText(t[0])
                    title1 = stripText(t[1])
                    org2 = stripText(t[2])
                    title2 = stripText(t[3])
                    if not not org1:
                        rels.add((name, org1, title1))

                    if not not org2:
                        rels.add((name, org2, title2))

                except Exception as e:
                    pass

        except Exception as e:
            pass

    # '据/p 机器之心/nt 了解/v ，/w 本文/r 作者/n 之/u 一/m 梁建明/nr 是/v 、/w AI医疗创业公司体素科技/nt 的/u 研究/vn 开发/ti 副总裁/ti ，/w 美国亚利桑那州立大学/nt （/w ASU/nz ）/w 副教授/ti ，/w 美国梅奥医学中心/nt 首届/m 入驻/vn 教授/ti ，/w 发表/v 了/u 超过/v 70篇/m 论文/n 并/c 获得/v 13项/m 专利/n 。/w'
    p9 = rules[6][8]
    for r in p9.findall(sent_pos):
        p10 = rules[6][9]
        for r1 in p10.findall(r[1]):
            p11 = rules[6][10]
            try:
                org = stripText(r1[0])
                title = ''.join(p11.findall(r1[1]))
                title = stripText(title)
                if org:
                    rels.add((name, org, title))
            except Exception as e:
                pass
    return rels, weight


def rule8(sent_pos):
    # '，/w 欧链/nt 科技/n 联合创始人/ti 谭智勇/nr 对/p 本报/n 记者/n 解释/v 道/v ，'
    global CURRENT_RULE
    CURRENT_RULE = 'rule8'
    p1 = rules[7][0]
    p2 = rules[7][1]
    rels = set()
    weight = 4

    for r in p1.findall(sent_pos):
        # print(r)
        try:
            title = stripText(r[1])
            name = stripText(r[2])

            org = ''.join([stripText(x) for x in p2.findall(r[0])])
            org = stripText(org)
            if name and org:
                rels.add((name, org, title))
        except Exception as e:
            pass
    return rels, weight


def rule9(sent_pos):
    # '对于/p 云计算/n 的/u 重要性/n ，/w 腾讯/nt 董事会/n 主席/n 兼/c 首席执行官/ti 马化腾/nr 多次/m 表示/v'
    global CURRENT_RULE
    CURRENT_RULE = 'rule9'
    p1 = rules[8][0]
    p2 = rules[8][1]
    rels = set()
    weight = 6

    for r in p1.findall(sent_pos):
        try:
            name = stripText(r[3])
            title1 = stripText(r[2])
            org = stripText(r[0])

            title2 = ''.join(p2.findall(r[1]))
            title2 = stripText(title2)
            if name and org:
                rels.add((name, org, title1))

                if not not title2:
                    rels.add((name, org, title2))
        except Exception as e:
            pass
    return rels, weight


# 与rule9兼字前后有直接显示ti的相反。
def rule10(sent_pos):
    # '对于/p 云计算/n 的/u 重要性/n ，/w 腾讯/nt 首席执行官/ti 兼/c 董事会/n 主席/n 马化腾/nr 多次/m 表示/v'
    global CURRENT_RULE
    CURRENT_RULE = 'rule10'
    p1 = rules[9][0]
    p2 = rules[9][1]
    rels = set()
    weight = 6

    for r in p1.findall(sent_pos):
        try:
            name = stripText(r[3])
            title1 = stripText(r[1])
            org = stripText(r[0])

            title2 = ''.join(p2.findall(r[2]))
            title2 = stripText(title2)
            if name and org:
                rels.add((name, org, title1))

                if not not title2:
                    rels.add((name, org, title2))
        except Exception as e:
            pass
    return rels, weight


def getRels(sent_pos):
    result_rels = set()

    rules = [
        rule1,
        rule2,
        rule3,
        rule4,
        rule5,
        rule6,
        rule7,
        rule8,
        rule9,
        rule10
    ]

    for rf in rules:
        rels, weight = rf(sent_pos)
        result_rels |= rels

    return result_rels
#返回一个set结构

if __name__ == '__main__':
    # text = '明略数据金融事业部/nt 解决方案专家/ti 杨昀/nr'
    # print('rule1', rule1(text))
    # text = '英特尔/nt CEO/ti Andy Grove/nr'
    # print('rule1', rule1(text))
    # text = '英诺天使基金/nz 创始合伙人/ti  /w 李竹/nr'
    # print('rule2', rule2(text))
    # text = '明略数据/nt 技术合伙人/ti 兼/v SCOPA/nz 产品经理/ti  /w 任鑫琦/nr'
    # print('rule3', rule3(text))
    # text = '059/m 、/w 郭欣/nr 。/w 美丽家/nt CEO/ti 。/w 帮助/v 设计师/n 和/c 施工队/n 跳出/v 装修/vn 公司/n 直接/ad 对接/v 房主/n ，/w 给/v 他们/r IT/n 能力/n ，/w 建立/v 信用/n 体系/n ，/w 家装业/n 的/u 淘宝/nz 。/w 监控宝/nt 创始人/ti ，/w 已/d 被/p 收购/v 。/w 愿/v 结交/v 有/v 梦想/n 有/v 激情/n 的/u 人/n 。/w'
    # print('rule7', rule7(text))
    # text = '069/m 、/w 杨俊峰/nr 。/w 广东恩集讴/ns 董事长/ti 。/w 做/v 了/u 10年/t 不锈钢/n 螺丝/n 钉/v 贸易/vn ，/w 年/n 销售/ti 额/xc 1.5亿/m ，/w 广东/ns 最大/a 。/w 2013年/t 进入/v 移动互联/nt 网/n ，/w 专注/v 于/p 活动/n 发布/vn 及/c 后续/vn 社交/n 服务/vn 。/w 创办/v “/w 协会网/nt ”/w ，/w 旗下/n APP/n ：/w “/w 云活动/nz ”/w 和/c “/w 云组织/nt ”/w ，/w 4月/t 上线/v 。/w'
    # print('rule7', rule7(text))
    # text = '中车株洲电力机车研究所有限公司/nt 副总经理/ti 、/w 总工程师/ti 冯江华/nr 则/c 对/p 未来/t 电池/n 的/u 发展/vn 做出/v 了/u 预估/vn 。/w'
    # print('rule5', rule5(text))
    # text = '美团/nt 的/u 王兴/nr 、/w 搜狗/nt 的/u CEO/ti 王小川/nr 、/w 英特尔/nt 的/u Andy Grove/nr 、/w 航班/n 管家/n 的/u 王江/nr 和/c 李黎军/nr 、/w 昆仑万维/nt 的/u 周亚辉/nr 、/w 柠檬微趣/nt 的/u 齐伟/nr 都是/v 。/w'
    # print('rule6', rule6(text))
    # text = './w Andy Grove/nr 是/v 一个/m 从/p 恐怖/a 统治/vn 中/f 逃离/v 的/u 匈牙利/ns 难民/n 。/w 他/r 学习/v 的/u 是/v 工程学/n ，/w 并/c 最终/ad 作为/v 英特尔/nt 的/u 首席执行官/ti 引领/v 了/u 个人电脑/n 革命/vn 。/w 他/r 与/p 帕金森病/nz 进行/v 了/u 长时间/n 的/u 斗争/vn ，/w 最终/ad 在/p 2016年/t 早些/t 时候/n ，/w 于/p 硅谷/ns 过世/v ，/w 享年/n 79岁/m 。/w'
    # print('rule7', rule7(text))
    # text = '，/w 欧链/nt 科技/n 联合创始人/ti 谭智勇/nr 对/p 本报/n 记者/n 解释/v 道/v ，'
    # print('rule8', rule8(text))
    # text = '对于/p 云计算/n 的/u 重要性/n ，/w 腾讯/nt 董事会/n 主席/n 兼/c 首席执行官/ti 马化腾/nr 多次/m 表示/v'
    # print('rule9', rule9(text))
    # text = '对于/p 云计算/n 的/u 重要性/n ，/w 腾讯/nt 首席执行官/ti 兼/c 董事会/n 主席/n 马化腾/nr 多次/m 表示/v'
    # print('rule10', rule10(text))
    # text = '武汉东川自来水科技开发有限公司/nt (/w 以下/f 简称/v “/w 武汉/ns 东川/ns ”/w )/w 董事长/ti 刘川/nr'
    # print('rule1', rule1(text))
    # text = '对此/d ，/w 58集团/nt 高级副总裁/ti 、/w 安居客/nt COO/ti 叶兵/nr 回应/v 称/v'
    # print('rule4', rule4(text))
    text = '据/p 机器之心/nt 了解/v ，/w 本文/r 作者/n 之/u 一/m 梁建明/nr 是/v AI医疗创业公司体素科技/nt 的/u 研究/vn 开发/ti 副总裁/ti ，/w 美国亚利桑那州立大学/nt （/w ASU/nz ）/w 副教授/ti ，/w 美国梅奥医学中心/nt 首届/m 入驻/vn 教授/ti ，/w 发表/v 了/u 超过/v 70篇/m 论文/n 并/c 获得/v 13项/m 专利/n 。/w'
    # print('rule7', rule7(text))
    text="腾讯的另一位创始人曾李青"
    from textProcessing import textprocess
    text=textprocess(text)
    print(text)
    ans=getRels(text)
    print(ans)
    #for i in ans:print(i,end=" ")
    # for i in ans:
    #     print(i[0])
