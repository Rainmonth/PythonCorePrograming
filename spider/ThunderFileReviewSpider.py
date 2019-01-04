#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 作者： RandyZhang
# 时间： 2018/11/9

import urllib.request
import ssl

from lxml import etree
import json

# %%
# 数据源分析
#
# 先请求到网页数据
# 分析网页数据
# 1. 浏览器请求目标网址，发现目标网页似乎是一个静态网站（其数据在网页加载成功后就一次性加载完了），只要找到其数据源就可以了
# 2. 发现页面底部的<script>标签中包含一个很长的字符串，其格式跟json字符串很像
# 3. 对该串稍加处理，发现可以很轻松的转换成json
# 4. 分析转换成的json，发现里面确实包含了我们需要的所用影评信息
# 5. 对得到的json进行处理，筛选出需要的信息，然后进行保存，如保存到文件、保存到数据库
#
# %%

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/52.0.2743.116 Safari/537.36",
    "Connection": "keep-alive"
}

context = ssl._create_default_https_context

# 目标网页：迅雷影评->天天精评
target_url = 'http://movie.xunlei.com/reviews/excellentreviews'


class ReviewItem:
    id = 0
    title = ''
    cover_url = ''
    summary = ''
    create_time = 0
    date = ''

    def __init__(self, _id, _title, _cover_url, _summary, _create_time, _date):
        self.id = _id
        self.title = _title
        self.cover_url = _cover_url
        self.summary = _summary
        self.create_time = _create_time
        self.date = _date

    def __str__(self) -> str:
        return super().__str__()


def get_html_data(url):
    print('目标url:' + url)
    req = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(req, context=context)
    # 解决中文乱码方法一：
    # htmldata = html.read().decode('utf-8')
    # 解决中文乱码方法二：
    htmlstr = str(response.read(), 'utf-8')
    htmlpath = etree.HTML(htmlstr)
    # 找到含有目标数据的script标签
    javascripts = htmlpath.xpath('//script[@type="text/javascript"]')
    jsondic = get_json_data(javascripts)
    get_all_reviews(jsondic)


def get_json_data(javascripts):
    if len(javascripts) == 1:
        jsonstr = str(javascripts[0].text).replace('window.__NUXT__=', '')
        jsonstr = jsonstr[0: len(jsonstr) - 1]
        fl = open('reviews.json', 'w')
        fl.write(jsonstr)
        jsondic = json.loads(jsonstr, encoding='utf-8')
        print(jsondic)
        return jsondic
    else:
        return None

    # print('tag->' + javascripts[0].tag)
    # print('text->' + javascripts[0].text)


def save_json_to_files(jsonstr):
    fl = open('reviews.json', 'w')
    fl.write(jsonstr)


def get_all_reviews(jsondic):
    """
    从json数据转换而来的字典中获取所有的影评数据
    :param jsondic: json数据转换而来的字典
    :return: 影评列表
    """
    if jsondic is not None:
        allreviewdic = jsondic['state']['reviews']['all']
        print('字典长度:' + str(len(allreviewdic)))
        allreviewlist = []
        for key in allreviewdic:
            reviewitem = allreviewdic[key]
            # reviewitem = ReviewItem(item['id'], item['title'], item['cover_url'], item['summary'],
            # item['create_time'], item['date'])
            print(reviewitem)
            allreviewlist.append(reviewitem)
        print('列表长度:' + str(len(allreviewlist)))
        return allreviewlist
    else:
        return None


if __name__ == '__main__':
    get_html_data(target_url)
