#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 作者： RandyZhang
# 时间： 2017/8/23
import urllib.request
import ssl

from lxml import etree

"""
#第一步: 从 http://www.nvshens.com/rank/sum/ 开始抓取MM点击头像的链接(注意是分页的)
#第二部: http://www.nvshens.com/girl/21751/ 抓取每一个写真集合的链接(注意是分页的)
#第三部: http://www.nvshens.com/g/19671/1.html 在写真图片的具体页面抓取图片(注意是分页的)
"""
piicturelist = []

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/52.0.2743.116 Safari/537.36",
    "Connection": "keep-alive"
}

context = ssl._create_unverified_context()

"""
从起始页面 http://www.nvshens.com/rank/sum/ 开始获取排名的页数和每一页的url
"""


def mmRankSum():
    req = urllib.request.Request("http://www.nvshens.com/rank/sum/", headers=header)
    html = urllib.request.urlopen(req, context=context)
    htmldata = html.read()
    htmlpath = etree.HTML(htmldata)

    # 首先获取页码数,然后用循环的方式挨个解析每一个页面
    pages = htmlpath.xpath('//div[@class="pagesYY"]/div/a/@href')

    for i in range(len(pages) - 2):
        pagesitem = "http://www.nvshens.com/rank/sum/" + pages[i]
        mmRankitem(pagesitem)


"""
参数 url : 分页中每一页的具体url地址
通过穿过来的参数，使用  lxml和xpath 解析 html，获取每一个MM写真专辑页面的url
"""


def mmRankitem(url):
    req = urllib.request.Request(url, headers=header)
    html = urllib.request.urlopen(req, context=context)
    htmldata = html.read()
    htmlpath = etree.HTML(htmldata)

    pages = htmlpath.xpath('//div[@class="rankli_imgdiv"]/a/@href')
    for i in range(len(pages)):
        print("http://www.nvshens.com/" + pages[i] + "album/")
        getAlbums("http://www.nvshens.com/" + pages[i] + "/album/")
        # print "http://www.nvshens.com/" + pages[i]


"""
参数 url : 每一个MM专辑的页面地址
通过穿过来的参数，获取每一个MM写真专辑图片集合的地址
"""


def getAlbums(girlUrl):
    req = urllib.request.Request(girlUrl, headers=header)
    html = urllib.request.urlopen(req, context=context)
    htmldata = html.read()
    htmlpath = etree.HTML(htmldata)

    pages = htmlpath.xpath('//div[@class="igalleryli_div"]/a/@href')
    for i in range(len(pages)):
        getPagePictures("http://www.nvshens.com/" + pages[i])


"""
参数 albumsUrl : 每一个MM写真专辑图片集合的地址
通过穿过来的参数，首先先获取图片集合的页数，然后每一页解析写真图片的真实地址
"""


def getPagePictures(albumsUrl):
    req = urllib.request.Request(albumsUrl, headers=header)
    html = urllib.request.urlopen(req, context=context)
    htmldata = html.read()
    htmlpath = etree.HTML(htmldata)
    pages = htmlpath.xpath('//div[@id="pages"]/a/@href')
    for i in range(len(pages) - 2):
        savePictures("http://www.nvshens.com" + pages[i])


"""
参数 itemPagesUrl : 每一个MM写真专辑图片集合的地址(进过分页检测)
通过穿过来的参数，直接解析页面，获取写真图片的地址，然后下载保存到本地。
"""


def savePictures(itemPagesUrl):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/52.0.2743.116 Safari/537.36",
        "Connection": "keep-alive",
        "Referer": "image / webp, image / *, * / *;q = 0.8",
        "Accept": "image/webp,image/*,*/*;q=0.8"
    }
    try:
        req = urllib.request.Request(itemPagesUrl, headers=header)
        html = urllib.request.urlopen(req, context=context)
        htmldata = html.read()
        htmlpath = etree.HTML(htmldata)
        print(itemPagesUrl)
        pages = htmlpath.xpath('//div[@class="gallery_wrapper"]/ul/img/@src')
        names = htmlpath.xpath('//div[@class="gallery_wrapper"]/ul/img/@alt')
    except Exception:
        pass
    for i in range(len(pages)):
        print(pages[i])
        piicturelist.append(pages[i])

        while len(piicturelist) > 100:
            saveUrlToTxtFile()
            break
        try:

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/52.0.2743.116 Safari/537.36",
                "Connection": "keep-alive",
                "Referer": "http://www.nvshens.com/img.html?img=" + pages[i]
            }
            req = urllib.request.Request(pages[i], headers=headers)

            urlhtml = urllib.request.urlopen(req, context=context)

            respHtml = urlhtml.read()

            binfile = open('/Users/RandyZhang/Pictures/ZnGirls/%s.jpg' % (names[i]), "wb")
            binfile.write(respHtml)
            binfile.close()
        except Exception:
            pass


def saveUrlToTxtFile():
    fl = open('list.txt', 'w')
    for i in piicturelist:
        fl.write(i)
        fl.write("\n")
    fl.close()


mmRankSum()

"""
print '关机ing'
print 'finish'
system('shutdown -s')
"""
