#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 描述： 翻译脚本（利用有道实现）
# 扩展： 将其装换成GUI形式，并实现可以切换翻译源的版本（可采用百度翻译、Google翻译）
# 作者： randy
# 时间： 2018/12/14 4:28 PM

# -*- coding:'utf-8' -*-
import requests
import json
import time

start = time.time()


def live():
    while True:
        content = input('输入你要翻译的:')
        if content == "e":
            break
        chrome = {
            "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        url = "https://fanyi.youdao.com/openapi.do?keyfrom=123licheng&key=1933182090&type=data&doctype=json&version=1.1&q={}".format(
            content)
        html = requests.get(url, headers=chrome)
        resqer = html.content
        load = json.loads(resqer)
        print(load["translation"][0])


live()
exit = time.time()
print('[+]该程序耗时', exit - start)
