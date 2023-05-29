#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Data_Analyse 
@File    ：greenhouse_gas_handle.py
@IDE     ：PyCharm 
@Author  ：Lsy
@Date    ：2023/5/29 16:03 
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['SimHei']
def greenhouse_gas_handle():
    data = pd.read_csv("Greenhouse_Gas.csv")
    data.info()
    data=data.drop('ISO2',axis=1)
    #可看出ISO2列无关数据分析可去除，其余数据均无缺失
    grouped=data.groupby('Country/Region')
    #对全球温室气体排放进行展示
    World_data=grouped.get_group('World')
    sum_data_World = World_data.loc[:, 'F2010':'F2021'].sum()
    x = ['F2010', 'F2011', 'F2012', 'F2013', 'F2014', 'F2015', 'F2016', 'F2017', 'F2018', 'F2019', 'F2020', 'F2021']
    plt.plot(x,sum_data_World.values)
    plt.title('Sum_World of F2010-F2021')
    plt.xlabel('Year')
    plt.ylabel('Sum')
    plt.show()
    #对东亚温室气体排放进行可视化
    EA_data=grouped.get_group('Eastern Asia')
    sum_data_EA = EA_data.loc[:, 'F2010':'F2021'].sum()
    x = ['F2010', 'F2011', 'F2012', 'F2013', 'F2014', 'F2015', 'F2016', 'F2017', 'F2018', 'F2019', 'F2020', 'F2021']
    plt.title('EA_Sum of F2010-F2021')
    plt.xlabel('Year')
    plt.ylabel('Sum')
    plt.plot(x,sum_data_EA.values)
    plt.show()

    #对全球二氧化碳排放量可视化分析
    Carbon_dioxide_data=World_data.groupby('Gas_Type').get_group('Carbon dioxide')
    sum_Carbon_dioxide_world=Carbon_dioxide_data.loc[:,'F2010':'F2021'].sum()
    plt.plot(x, sum_Carbon_dioxide_world.values)
    plt.title('Carbon_Sum_World of F2010-F2021')
    plt.xlabel('Year')
    plt.ylabel('Sum')
    plt.show()
    # 对数据进行归一化
    # normalized_data = (sum_Carbon_dioxide_world - sum_Carbon_dioxide_world.mean()) / sum_Carbon_dioxide_world.std()
    # plt.plot(x, normalized_data.values)
    # plt.title('Carbon_Sum_World of F2010-F2021')
    # plt.xlabel('Year')
    # plt.ylabel('Sum')
    # plt.show()
    # print(normalized_data)

    print(sum_Carbon_dioxide_world)