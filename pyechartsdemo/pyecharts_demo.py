#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd

from pyecharts import Bar, Style
from pyecharts import Polar

input_file_path = '../inputfiles/pyecharts/'
output_file_path = '../outputfiles/pyecharts/'


def print_demo_head(demo_name, need_enter=True):
    if need_enter:
        print('\n')
    print('*' * 100)
    print(demo_name)
    print('*' * 100)


def generate_aqi_bar_chart():
    # 展示各城市AQI（空气质量指数）
    data_1 = pd.read_excel(input_file_path + '20180630空气质量指数.xlsx', sheet_name=0)
    print(data_1.head())
    x = data_1.columns.tolist()
    y = data_1.loc['AQI'].tolist()
    # 标题和附表题
    bar = Bar('各城市AQI', '2018年6月30日')
    bar.add('AQI', x, y, mark_point=['max'], mark_line=['average'], label_color=['#9932CC'])
    bar.render(output_file_path + 'htmls/PyCharm各城市AQI柱状图.html')


def generate_kfc_dks_distribute_bar_chart():
    """
    生成肯德基、德克士分布图
    :return:
    """
    # 读取数据
    data = pd.read_excel(input_file_path + '省会城市KFC_MC_德克士.xlsx', sheet_name=0)
    print(data.head())
    city = data['城市'].tolist()
    mc_num = data['麦当劳店面数量'].tolist()
    kfc_num = data['KFC店面数量'].tolist()
    dks_num = data['德克士店面数量'].tolist()

    # 设置样式
    style = Style(title_pos='center', width=1000, height=500, background_color='white')
    bar_style = style.add(legend_top='bottom',  # 图例位置
                          yaxis_rotate=45,  # Y轴标签旋转角度
                          label_color=[' #FFB90F', '#FFF68F', '#1E90FF'])  # 柱状图颜色
    bar = Bar('省会城市快餐店数量', **style.init_style)
    bar.add('麦当劳', city, mc_num, is_stack=True, is_convert=False, **bar_style)  # 是否堆积，是否反转
    bar.add('肯德基', city, kfc_num, is_stack=True, is_convert=False, **bar_style)  # 是否堆积，是否反转
    bar.add('德克士', city, dks_num, is_stack=True, is_convert=False, **bar_style)  # 是否堆积，是否反转
    bar.render(output_file_path + 'htmls/省会城市快餐店数量堆积柱状图.html')


def generate_kfc_dks_distribute_polar_bar_chart():
    # 读取数据
    data = pd.read_excel(input_file_path + '省会城市KFC_MC_德克士.xlsx', sheet_name=0)
    print(data.head())
    city = data['城市'].tolist()
    mc_num = data['麦当劳店面数量'].tolist()
    kfc_num = data['KFC店面数量'].tolist()
    dks_num = data['德克士店面数量'].tolist()
    radius = city
    polar = Polar('省会城市快餐店数量', width=1200, height=600)
    polar.add('', mc_num, radius_data=radius, type='barAngle', is_stack=True)
    polar.add('', kfc_num, radius_data=radius, type='barAngle', is_stack=True)
    polar.add('', dks_num, radius_data=radius, type='barAngle', is_stack=True)
    polar.render(output_file_path + 'htmls/省会城市快餐店数量极坐标堆叠柱状图.html')


if __name__ == '__main__':
    print_demo_head('AQI指数', False)
    generate_aqi_bar_chart()

    print_demo_head('省会城市KFC、德克士分布图')
    generate_kfc_dks_distribute_bar_chart()

    print_demo_head('省会城市KFC、德克士极坐标分布图')
    generate_kfc_dks_distribute_polar_bar_chart()
