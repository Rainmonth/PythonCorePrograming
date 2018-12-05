#!/usr/local/bin/python
# -*- coding: UTF-8 -*-
import calendar

cal = calendar.month(2016, 1)
print("以下输出2016年1月份的日历:")
print(cal)

# python3.6
calendar_text = calendar.TextCalendar()
# 打印月历
calendar_text.prmonth(2017, 5, w=0, l=0)

# 打印年历
calendar_text.pryear(2017, w=2, l=1, c=6, m=3)
