#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 描述： python 文件操作，相关模块：os、shutil->文件拷贝、struct->二进制支持
# 作者： randy
# 时间： 2019/1/4 4:50 PM

import os
import shutil


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
    """
    只能删除空目录
    :param dirpath:
    :return:
    """
    if not os.path.isdir(dirpath):
        print(dirpath + '不是合法的目录')
        return
    os.rmdir()


def rmdirs(rootdir):
    """
    只能从深到浅依次删除空目录，遇到非空目录结束
    """
    if not os.path.isdir(rootdir):
        print(rootdir + '不是合法的目录')
        return
    os.removedirs(rootdir)


def rmtress(rootdir):
    try:
        if not os.path.isdir(rootdir):
            print(rootdir + '不是合法的目录')
            return
        shutil.rmtree(rootdir)
    except Exception as e:
        print(e)
        return


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
    :param new: new如果是相对路径，直接在当前目录创建文件
    :return:
    """
    try:
        os.rename(old, new)
    except Exception as e:
        print(e)


def cpfile(oldfile, newfile):
    """
    文件复制(oldfile必须都是文件,newfile可以是文件或文件夹)
    :param oldfile: 待复制的文件
    :param newfile: 目标文件或文件夹
    :return:
    """
    try:
        return shutil.copy(oldfile, newfile)
    except Exception as e:
        print(e)
        return None


def cpfilewithstate(srcfile, dstpath):
    """
    文件复制(oldfile必须都是文件,newfile可以是文件或文件夹)
    :param srcfile: 待复制的文件
    :param dstpath: 目标文件或文件夹
    :return:
    """
    try:
        return shutil.copy2(srcfile, dstpath)
    except Exception as e:
        print(e)
        return None


def cptree(olddir, newdir):
    try:
        if direxist(newdir):
            rmtress(newdir)
        return shutil.copytree(olddir, newdir)
    except Exception as e:
        print(e)
        return None


def move(oldpos, newpos):
    try:
        return shutil.move(oldpos, newpos)
    except Exception as e:
        print(e)
        return None


def writetofile(filepath, content):
    try:
        filedir, filename = os.path.split(filepath)
        fl = openfile(filedir, filename, 'w')
        if fl is not None:
            fl.write(content)
            fl.close()
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def appendtofile(filepath, content):
    try:
        filedir, filename = os.path.split(filepath)
        fl = openfile(filedir, filename, 'a')
        if fl is not None:
            fl.write(content)
            fl.close()
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def getfiledir(filepath):
    return os.path.dirname(filepath)


def getfilename(filepath):
    return os.path.basename(filepath)


def getfileext(filename):
    if not os.path.isfile(filename):
        print('不是有效文件')
        return
    else:
        return os.path.splitext(filename)[1]


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
    # filehandler = openfile(str(curdir()) + os.path.sep + 'name', 'test.txt', 'w')
    # filehandler.write("teststrsssss")

    # mkdir(curdir() + os.path.sep + 'name' + os.path.sep + 'test')

    # renamefile(curdir() + os.path.sep + 'name' + os.path.sep + 'test.txt',
    #            curdir() + os.path.sep + 'name' + os.path.sep + 'test1.txt')

    # print(os.path.isdir('/Users/randy/Desktop'))
    # print(listdir('/Users/randy/Desktop'))
    #
    # print(rmdirs('/Users/randy/Desktop/test/a/b/c'))

    # print(cpfile('/Users/randy/Desktop/test/a/a.txt', '/Users/randy/Desktop/test/b/a.txt'))

    print(shutil.copy('/Users/randy/Desktop/test/a/a.txt', '/Users/randy/Desktop/test/b'))
