#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys

from PIL import Image
import os


def open_image(path, name):
    try:
        im = Image.open(path + os.sep + name)
        # 打印图片格式、尺寸、色彩模式
        print(im.format, im.size, im.mode)
        # 采用系统默认打开方式打开文件
        im.show()
    except Exception as e:
        print(e)


def convert_to_jpeg(path, name):
    print(path + os.sep + name)
    infile = path + os.sep + name
    f, e = os.path.splitext(infile)
    outfile = f + '.jpg'
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print('can not convert ', infile)


if __name__ == '__main__':
    # open_image('.', 'pil_test.jpg')

    convert_to_jpeg('.', 'pil_test.png')
