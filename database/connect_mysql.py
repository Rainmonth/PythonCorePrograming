#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pymysql

cxn = pymysql.connect(host='127.0.0.1', user='root', passwd='zh7359431', port=3306)
cur = cxn.cursor()
cur.execute('show databases;')
cur.execute('create database if not EXISTS test;')
cur.execute('use test;')
cur.execute('CREATE TABLE if not EXISTS users(login VARCHAR(8), userid INT)')
cur.execute("INSERT INTO users VALUES('john', 7000)")
cur.execute("INSERT INTO users VALUES('jane', 7001)")
cur.execute("INSERT INTO users VALUES('bot', 7200)")

cur.execute("SELECT * FROM users WHERE login LIKE 'j%'")

for data in cur.fetchall():
    print('%s\t%s' % data)

cur.execute("UPDATE users SET userid=7100 WHERE userid=7001")

cur.execute("SELECT * FROM users")

for data in cur.fetchall():
    print('%s\t%s' % data)

cur.execute('DELETE FROM users WHERE login="bot"')

cur.execute("SELECT * FROM users")

for data in cur.fetchall():
    print('%s\t%s' % data)

cur.execute('DROP TABLE users')

cur.close()
cxn.commit()
cxn.close()
