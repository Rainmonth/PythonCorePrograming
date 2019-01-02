#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 单线程示例


from time import sleep, ctime


def loop0():
    print('start loop0 at: ', ctime())
    sleep(4)
    print('end loop0 at: ', ctime())


def loop1():
    print('start loop1 at: ', ctime())
    sleep(2)
    print('end loop1 at: ', ctime())


def main():
    print('starting at: ', ctime())
    loop0()
    loop1()
    print('all done at: ', ctime())


if __name__ == '__main__':
    main()
