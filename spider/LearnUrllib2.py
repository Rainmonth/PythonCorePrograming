#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 作者： RandyZhang
# 时间： 2018/10/18

import urllib.request

"""
构建请求与响应模型
"""


def createReqResMode(requestUrl):
    response = urllib.request.urlopen(requestUrl)
    data = response.read()
    data = data.decode("utf-8")
    print(data)


createReqResMode("http://rainmonth.cn")

"""
Get与Post传递数据
"""


def makeGetRequest():
    print("Get Request")


def makePostRequest():
    print("Post Request")
