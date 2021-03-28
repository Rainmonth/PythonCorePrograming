#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd

from pyecharts import Bar, Style
from pyecharts import Polar
from pyecharts import Bar3D
from pyecharts import HeatMap

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
    # polar = Polar('省会城市快餐店数量', width=1200, height=600)
    # polar.add('', mc_num, radius_data=radius, type='barAngle', is_stack=True)
    # polar.add('', kfc_num, radius_data=radius, type='barAngle', is_stack=True)
    # polar.add('', dks_num, radius_data=radius, type='barAngle', is_stack=True)
    # polar.render(output_file_path + 'htmls/省会城市快餐店数量极坐标堆叠柱状图.html')

    polar = Polar('省会城市快餐店数量', width=1200, height=1200)
    polar.add('', mc_num, radius_data=radius, type='barRadius', is_stack=True)
    polar.add('', kfc_num, radius_data=radius, type='barRadius', is_stack=True)
    polar.add('', dks_num, radius_data=radius, type='barRadius', is_stack=True)
    polar.render(output_file_path + 'htmls/省会城市快餐店数量极坐标分类堆叠柱状图.html')


def generate_3d_bar_chart():
    data = pd.read_excel(input_file_path + '每日销量.xlsx', sheet_name=0)
    print(data.head())
    x_axis = data['week'].tolist()
    data['week'] = data['week'].str.replace('week', '').map(int) - 1
    data = data.set_index('week')
    y_axis = data.columns.tolist()
    data.columns = range(0, 7)
    data = data.stack().reset_index()
    data.columns = ['week', 'day', 'amount']
    print(data.head())
    style = Style(
        title_color='#A52A2A',
        title_pos='center',
        width=900,
        height=1100,
        background_color='#ABABAB'
    )
    style_3d = style.add(
        is_visualmap=True,
        visual_range=[0, 120],
        visual_range_color=['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
                            '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026'],
        grid3d_width=200,
        grid3d_depth=80,
        xaxis_label_textcolor='#fff',
        is_grid3d_rotate=True,
        legend_pos='right'
    )
    bar3d = Bar3D('全年产量情况', **style.init_style)
    bar3d.add('每日产量', x_axis, y_axis, data.values.tolist(), **style_3d)
    bar3d.render(output_file_path + 'htmls/全年产量情况3D柱状图.html')


def generate_heatmap():
    data = pd.read_excel(input_file_path + '每日销量.xlsx', sheet_name=0)
    print(data.head())
    x_axis = data['week'].tolist()
    data['week'] = data['week'].str.replace('week', '').map(int) - 1
    data = data.set_index('week')
    y_axis = data.columns.tolist()
    data.columns = range(0, 7)
    data = data.stack().reset_index()
    data.columns = ['week', 'day', 'amount']
    heatmap = HeatMap()
    heatmap.add('全年产量情况', x_axis, y_axis, data.values.tolist(), is_visualmap=True,
                visual_text_color="#000", visual_orient='horizontal')
    heatmap.render(output_file_path + 'htmls/全年产量情况热力图.html')


if __name__ == '__main__':
    # print_demo_head('AQI指数', False)
    # generate_aqi_bar_chart()
    #
    # print_demo_head('省会城市KFC、德克士分布图')
    # generate_kfc_dks_distribute_bar_chart()
    #
    # print_demo_head('省会城市KFC、德克士极坐标分布图')
    # generate_kfc_dks_distribute_polar_bar_chart()
    print_demo_head('全年产量3D柱状图')
    generate_3d_bar_chart()

    # print_demo_head('全年产量热力图')
    # generate_heatmap()
