#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Data_Analyse
@File    ：Forest_Cover.py
@IDE     ：PyCharm
@Author  ：Lsy
@Date    ：2023/5/30 17:50
'''

'''
数据解读：
该数据为全球各国森林覆盖面积（1990-2020）及土地面积总和
单位为*1000公顷
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def Forest_Cover():
    data=pd.read_csv("Data_Source/fra2020-extentOfForest.csv")
    data.info()
    world_data=data.iloc[:,1:]
    world_data=world_data.sum()
    Total_area=world_data.values[-1]
    names=list(world_data.index)[:-1]
    values=world_data.values[:-1]
    rate=[]
    for value in values:
        rate.append(value/Total_area)
    print(names)
    print(values)
    print(rate)
    '''
    绘制折线图
    --森林占地面积比率折线图
    '''
    plt.plot(names, rate)
    plt.xlabel('Year')
    plt.ylabel('Ratio of Forest Area to Total Area')
    plt.title('Global Forest Area Ratio (1990-2020)')

    # 显示图形
    plt.show()

    '''
        森林占地面积柱状图
    '''
    plt.bar(names, values)
    # 设置图表属性
    plt.xlabel('Year')
    plt.ylabel('Forest Area (hectares)')
    plt.title('Global Forest Area (1990-2020)')
    # 显示图形
    plt.show()
    '''
    森林占地面积与总面积比率饼图
    '''
    plt.pie(rate, labels=names, autopct='%1.1f%%')
    # 设置图表属性
    plt.title('Global Forest Area Ratio (1990-2020)')
    # 显示图形
    plt.show()
Forest_Cover()