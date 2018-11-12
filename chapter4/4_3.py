#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 多线程示例（使用线程和锁）

import _thread
from time import sleep, ctime

loops = [14, 2, 8]


def loop(nloop, nsec, lock):
    print(nloop, 'start at:', ctime())
    sleep(nsec)
    print(nloop, 'done at:', ctime())
    lock.release()


def main():
    print('starting at:', ctime())
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked():
            pass

    print('all done at:', ctime())


if __name__ == '__main__':
    main()
