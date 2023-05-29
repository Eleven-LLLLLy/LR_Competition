#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Data_Analyse 
@File    ：11.py
@IDE     ：PyCharm 
@Author  ：Lsy
@Date    ：2023/5/26 15:43 
'''
import matplotlib.pyplot as plt
import numpy as np

# 生成数据
years = np.array([2016, 2017, 2018, 2019, 2020])
a_data = np.array([100, 120, 150, 180, 200])
b_data = np.array([80, 100, 120, 150, 170])

# 绘制柱状图
bar_width = 0.35
plt.bar(years, a_data, bar_width, label='a')
plt.bar(years + bar_width, b_data, bar_width, label='b')

# 设置图表标题和坐标轴标签
plt.title('Yearly Data')
plt.xlabel('Year')
plt.ylabel('Quantity')

# 添加图例
plt.legend()

# 显示图表
plt.show()
