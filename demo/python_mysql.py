#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 描述： python mysql 数据库操作
# 作者： randy
# 时间： 2019/1/3 7:04 PM

import pymysql

DB_HOST = '127.0.0.1'
DB_USER = 'root'
DB_PORT = 3306
DB_NAME = 'pytest'


def connectdb():
    dbhost = input('输入数据库地址：')
    dbuser = input('输入数据库用户名：')
    dbpwd = input('输入数据库密码：')
    dbname = input('输入数据库名：')
    dbport = input('请输入端口号：')
    db = pymysql.connect(dbhost, dbuser, dbpwd, dbname, int(dbport))
    if db:
        print('数据库连接成功')
        return db
    else:
        print('数据库连接失败')
        return


def direct_connect(dbhost='127.0.0.1', dbuser=None, dbpwd=None, dbname='pytest', dbport=3306):
    if dbuser is None:
        print('用户名为None')
        return
    if dbpwd is None:
        print('密码为None')
        return
    db = pymysql.connect(dbhost, dbuser, dbpwd, dbname, dbport)
    if db:
        print('数据库连接成功')
        return db
    else:
        print('数据库连接失败')
        return


def ctable():
    pass


def insert():
    pass


def delete():
    pass


def update():
    pass


def query():
    pass


def exesql():
    """
    执行sql语句
    :return:
    """
    pass


if __name__ == '__main__':
    connectdb()
