#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 作者： RandyZhang
# 时间： 2017/8/1

from time import ctime
from urllib.request import urlopen

TICKs = ('yhoo', 'dell', 'cost', 'adbe', 'intc')
URL = 'http://quote.yahoo.com/d/quotes.csv?s=%s&f=sllcip2'

print('\nPrices quoted as of: %s PDT\n' % ctime())
print('TICKET', 'PRICE', 'CHANGE', '%AGE')
print('------', '-----', '------', '----')
u = urlopen(URL % ','.join(TICKs))

for row in u:
    tick, price, chg, per = row.split(',')
    print(tick, '%.2f' % float(price), chg, per, u.close())
