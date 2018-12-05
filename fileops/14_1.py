#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 保存csv数据，并读取保存的数据

import csv
from distutils.log import warn as printf

DATA = (
    (9, 'Web Clients and Servers', 'base64, urllib'),
    (10, 'Web Programming : CGI & WSGI', 'cgi, time, wsgiref'),
    (13, 'Web Services', 'urllib, twython'),
)

printf('*** WRITING CSV DATA')
f = open('bookdata.csv', 'w')
writer = csv.writer(f)
for record in DATA:
    writer.writerow(record)
f.close()

printf('*** REVIEW OF SAVED DATA')
f = open('bookdata.csv', 'r')
reader = csv.reader(f)
for chap, title, modpkgs in reader:
    printf('Chapter %s:%r (featuring %s)' % (chap, title, modpkgs))
f.close()
