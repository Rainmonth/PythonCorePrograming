#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 多线程示例（使用threading——传递一个函数来创建threading的实例）

import threading
from time import sleep, ctime

loops = [14, 2, 8]


def loop(nloop, nsec):
    print(nloop, 'start at:', ctime())
    sleep(nsec)
    print(nloop, 'done at:', ctime())


def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))  # 传递一个函数
        threads.append(t)

    for i in nloops:
        threads[i].start()  # 开始所有线程

    for i in nloops:
        threads[i].join()  # 在启动线程终止之前一直挂起（等待所有子线程终止）

    print('all done at:', ctime())


if __name__ == '__main__':
    main()
