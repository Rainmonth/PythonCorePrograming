#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 描述： python 文件操作
# 作者： randy
# 时间： 2019/1/4 4:50 PM

import os


def curdir():
    result = os.getcwd()
    print('当前目录->' + result)
    return result


def listdir(rootdir):
    if os.path.isdir(rootdir) and os.path:
        return os.listdir(rootdir)


def rmfile(filepath):
    if not os.path.isfile(filepath):
        print(filepath + '不是合法的文件')
        return
    os.remove(filepath)


def rmdir(dirpath):
    if not os.path.isdir(dirpath):
        print(dirpath + '不是合法的目录')
        return
    os.rmdir()


def rmdirs(rootdir):
    if not os.path.isdir(rootdir):
        print(rootdir + '不是合法的目录')
        return
    os.removedirs(rootdir)


def fileexist(filapath):
    result = os.path.exists(filapath)
    if result:
        print(filapath + '存在')
    else:
        print(filapath + '不存在')
    return result


def isabspath(path):
    result = os.path.isabs(path)
    if result:
        print(path + '是绝对路径')
    else:
        print(path + '不是绝对路径')
    return result


def direxist(dirpath):
    result = os.path.exists(dirpath)
    if result:
        print(dirpath + '是一个有效文件目录')
    else:
        print(dirpath + '不是一个有效文件目录')
    return result


def mkdir(dirpath, dirmode=0o777):
    try:
        if isinstance(dirmode, int):
            if not os.path.exists(dirpath):
                os.mkdir(dirpath, dirmode)
            else:
                print(dirpath + '已经存在，无需创建')
        else:
            print('dirmode需为int型')
            return
    except Exception as e:
        print(e)
        return


def mkdirs(dirpath, dirmode=0o777):
    try:
        if isinstance(dirmode, int):
            if not os.path.exists(dirpath):
                os.makedirs(dirpath, dirmode)
            else:
                print(dirpath + '已经存在，无需创建')
        else:
            print('dirmode需为int型')
            return
    except Exception as e:
        print(e)
        return


def openfile(dirpath, filename, filemode='w'):
    try:
        if not direxist(dirpath):
            mkdir(dirpath)
        fl = open(dirpath + os.path.sep + filename, filemode)

        return fl
    except Exception as e:
        print(e)
        return None


def renamefile(old, new):
    """

    :param old:
    :param new: new如果是相对路径
    :return:
    """
    os.rename(old, new)


def cpfile(frompath, topath):
    pass


def writetofile(filepath, content):
    pass


def appendtofile(filepath, content):
    pass


def getfiledir(filepath):
    return os.path.dirname(filepath)


def getfilename(filepath):
    return os.path.basename(filepath)


def getsize(filepath):
    try:
        return os.path.getsize(filepath)
    except Exception as e:
        print(e)
        return


if __name__ == '__main__':
    # curdir()
    # fileexist('/Users/randy/PycharmProjects/PythonLearning/toolkits/fileutil.py')
    # direxist('/Users/randy/PycharmProjects/PythonLearning/toolkits')
    # isabspath('fileutil.py')
    # print(str(curdir()))
    # os.makedirs(str(curdir()) + '/test.txt', 0o777)
    filehandler = openfile(str(curdir()) + os.path.sep + 'name', 'test.txt', 'w')
    filehandler.write("teststrsssss")

    mkdir(curdir() + os.path.sep + 'name' + os.path.sep + 'test')

    renamefile(curdir() + os.path.sep + 'name' + os.path.sep + 'test.txt',
               curdir() + os.path.sep + 'name' + os.path.sep + 'test1.txt')

    # print(os.path.isdir('/Users/randy/Desktop'))
    # print(listdir('/Users/randy/Desktop'))
    #
    # print(rmdirs('/Users/randy/Desktop/test/a/b/c'))
