#coding:utf-8
import re
SPLIT_LINE_MARKER = '！'
SPLIT_LINE_MARKER_SIZE = 3
client = baiduSegmentClient()


# 拆分为句子
def sentencesMaker(html):
    sentences = []
    if not html or not html.strip():
        return sentences
    try:
        import re
        html = re.sub(r'(\\n)|(\n)', '', html)
        import justext
        from html.parser import unescape
        html = unescape(html)
        paragraphs = justext.justext(html, [])

        cache_sentences = ''

        for p in paragraphs:
            sent = p.text.strip().replace('\xa0', '').replace('\u3000', '')
            sent = sent.encode('gb2312', 'ignore').decode('gb2312').encode('gbk', 'ignore').decode('gbk')
            if not sent:
                continue

            # 可能是含有名字，需要进一步处理
            if len(cache_sentences) < 5:
                cache_sentences += ' ' + sent
            else:
                sentences.append(cache_sentences.strip())
                cache_sentences = sent

        if not not cache_sentences:
            sentences.append(cache_sentences.strip())
    except Exception as e:
        logger.error(e)

    return sentences


# 重新恢复句子,并返回相关的
def restoreSentences(text):
    restore_sentences = []
    if text is None:
        return restore_sentences

    result = client.lexerCustom(text)

    items = result.get('items', [])
    items_size = len(items)

    tries_limit = 5
    tries_counter = 0
    while items_size == 0:
        if len(text) != 0:
            # 可能是qps限制
            time.sleep(0.5)
            result = client.lexerCustom(text)

            items = result.get('items', [])
            items_size = len(items)

        tries_counter += 1

        if tries_counter >= tries_limit:
            logger.error('error: 分词api请求失败多次！')
            return restore_sentences

    restore_idx = 0

    last_restore_idx = 0
    has_per = False

    while restore_idx < items_size:
        # TODO 需要做的
        while restore_idx < items_size and items[restore_idx]['item'] != SPLIT_LINE_MARKER:
            item = items[restore_idx]
            # TODO 剔除机构中的不合法字符
            format_pos = item['pos']

            if item['ne'].startswith('ORG') or format_pos == 'nt':
                invalid_orgs = [
                    '公司',
                    '我的'
                ]
                item['item'] = item['item'].replace('&', '')
                if item['item'] in invalid_orgs:
                    format_pos = 'n'
                else:
                    format_pos = 'nt'

            elif item['ne'] == 'PER':
                format_pos = 'nr'

            elif item['ne'] == 'TITLE':
                format_pos = 'ti'

            elif item['ne'] == 'LOC':
                format_pos = 'ns'

            elif item['ne'] == 'TIME':
                format_pos = 't'

            if format_pos == '':
                format_pos = 'xx'

            elif format_pos == 'nr':
                # 过滤先生或者女士之类的名称
                name = re.sub(r'((先生)|(小姐)|(阿姨)|(叔叔)|(女士)|(同志)|总|(博士)|(老师))$', '', item['item'])

                if len(name) >= 2:
                    invalid_names = {
                        '区块链': 'n'
                    }

                    if name not in invalid_names:
                        has_per = True
                        item['item'] = name
                    else:
                        format_pos = invalid_names[name]

                else:

                    format_pos = 'n'

            item['pos'] = format_pos

            # 删除无用信息
            item.pop('basic_words')
            item.pop('formal')
            item.pop('byte_length')
            item.pop('byte_offset')
            item.pop('loc_details')
            item.pop('ne')
            item.pop('uri')

            items[restore_idx] = item
            restore_idx += 1

        if restore_idx + SPLIT_LINE_MARKER_SIZE - 1 < items_size:
            needCut = True
            for i in range(SPLIT_LINE_MARKER_SIZE - 1):
                if items[restore_idx + i + 1]['item'] != SPLIT_LINE_MARKER:
                    needCut = False
                    break

            if needCut:
                # 看看下一个是不是SPLIT_LINE_MARKER，若是，可能需要偏移一位
                step = 0
                while restore_idx + SPLIT_LINE_MARKER_SIZE + step < items_size \
                        and items[restore_idx + SPLIT_LINE_MARKER_SIZE + step] == SPLIT_LINE_MARKER:
                    step += 1

                restore_idx += step

                ed = max(restore_idx, 0)

                sentence_items = items[last_restore_idx:ed]
                if len(sentence_items) != 0:
                    # print('per:', sentence_items)
                    restore_sentences.append((sentence_items, has_per))

                next_st = min(ed + SPLIT_LINE_MARKER_SIZE, items_size)
                last_restore_idx = next_st

                restore_idx += SPLIT_LINE_MARKER_SIZE
            else:
                restore_idx += 1

        else:
            ed = max(restore_idx, 0)
            sentence_items = items[last_restore_idx:ed]
            if len(sentence_items) != 0:
                restore_sentences.append((sentence_items, has_per))

            restore_idx = items_size

        has_per = False

    # print(restore_sentences)
    return restore_sentences


# 解析并标注HTML
def posHtml(html):
    sentences = sentencesMaker(html)

    cut_str = ''

    pos_sentences = []

    for sent in sentences:
        sent = sent.strip()
        if not sent:
            continue
        if not cut_str:
            tmp_str = sent
        else:
            tmp_str = cut_str + SPLIT_LINE_MARKER * SPLIT_LINE_MARKER_SIZE + sent
        if sys.getsizeof(tmp_str) < 3700:
            cut_str = tmp_str
        else:
            try:
                # time.sleep(0.3)
                pos_sentences += restoreSentences(cut_str)

            except Exception as e:
                logger.error('error: ', sent)
                logger.error(e)

            cut_str = sent

    if not not cut_str:
        # time.sleep(0.3)
        try:
            pos_sentences += restoreSentences(cut_str)
        except Exception as e:
            logger.error('error: ', sent)
            logger.error(e)

    return pos_sentences
