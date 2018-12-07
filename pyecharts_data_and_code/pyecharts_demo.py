#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd

from pyecharts import Bar


def generate_aqi_bar_chart():
    # 展示各城市AQI（空气质量指数）
    data_1 = pd.read_excel('./20180630空气质量指数.xlsx', sheet_name=0)
    print(data_1.head())
    x = data_1.columns.tolist()
    y = data_1.loc['AQI'].tolist()
    # 标题和附表题
    bar = Bar('各城市AQI', '2018年6月30日')
    bar.add('AQI', x, y, mark_point=['max'], mark_line=['average'], label_color=['#9932CC'])
    bar.render('./参考案例HTML/PyCharm各城市AQI柱状图.html')


if __name__ == '__main__':
    generate_aqi_bar_chart()
