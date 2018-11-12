#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 图书排名
import ssl
from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib.request import urlopen as uopen

# 匹配数字和逗号，并以 in Books结尾
REGEX = compile('#([\d,]+) in Books')
AMZN = 'http://amazon.com/dp/'
ISBNS = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals',
}

user_agent = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/59.0.3071.115 Mobile Safari/537.36'

context = ssl._create_unverified_context()


def get_ranking(isbn):
    url = '%s%s' % (AMZN, isbn)
    # headers = {'User-Agent': user_agent}
    # req = Request(url, headers=headers)
    print('request url:', url)
    try:
        # python3 需要加上context，否则报错<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED]
        # certificate verify failed (_ssl.c:748)>
        page = uopen(url, timeout=30, context=context)  # or use str.format()
        print('Open', url, 'success')
        data = page.read()
        # python3，必须要加这句，否则会报错：TypeError: cannot use a string pattern on a bytes-like object
        data = data.decode('utf-8')
        page.close()
        result = REGEX.findall(data)
        return result[0]
    except Exception as e:
        print(str(e))
    return 'unknow'


def _show_ranking(isbn):
    print('- %r ranked %s' % (ISBNS[isbn], get_ranking(isbn)))


def _main():
    print('At', ctime(), 'on Amazon...')
    for isbn in ISBNS:
        # _show_ranking(isbn)  #单线程
        Thread(target=_show_ranking, args=(isbn,)).start()  # 多线程


@register
def _atexit():
    print('All done at', ctime())


if __name__ == '__main__':
    _main()
