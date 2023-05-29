#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Data_Analyse 
@File    ：test.py
@IDE     ：PyCharm 
@Author  ：Lsy
@Date    ：2023/5/22 16:48 
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
def Temp_handle():
    data=pd.read_csv("Temp.csv")
    #ISO2、ISO3、Indicator等数据与本次数据无关则直接清除
    data = data.drop(['ISO2','ISO3','Indicator','Unit','Source','CTS_Code','CTS_Name','CTS_Full_Descriptor'], axis=1)
    data.info()
    grouped = data.groupby('Country/Region')
    # 对全球温室气体排放进行展示
    World_data = grouped.get_group('World').loc[:,'F2010':'F2021'].sum()
    x = ['F2010', 'F2011', 'F2012', 'F2013', 'F2014', 'F2015', 'F2016', 'F2017', 'F2018', 'F2019', 'F2020', 'F2021']
    plt.plot(x, World_data.values)
    plt.title('Tempchange of F2010-F2021')
    plt.xlabel('Year')
    plt.ylabel('change_rate')
    plt.show()
def Energy_handle():
    '''数据处理，针对国家、类型进行分类，并选定特定年份'''
    data=pd.read_csv('Energy_Transition.csv')
    data=data.groupby('Country/Region')
    data=data.get_group('World')
    data=data.groupby('Energy_Type')
    data_renew=data.get_group('Total Renewable')
    data_Non_renew=data.get_group('Total Non-Renewable')
    data_renew=data_renew.loc[:,'F2010':'F2020']
    data_Non_renew = data_Non_renew.loc[:, 'F2010':'F2020']

    '''对数据进行统计'''
    x=np.array([2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020])
    non_renew_data=np.array(data_Non_renew.sum().values.tolist())
    renew_data=np.array(data_renew.sum().values.tolist())

    '''计算两种类型增长率'''
    renew_growth = np.diff(renew_data) / renew_data[:-1] * 100
    nonrenew_growth = np.diff(non_renew_data) / non_renew_data[:-1] * 100
    '''绘制柱形图以及增长曲线图'''
    fig, ax1 = plt.subplots(figsize=(8, 6))
    bar_width = 0.35
    ax1.bar(x, renew_data, bar_width, label='renew')
    ax1.bar(x+bar_width , non_renew_data, bar_width, label='non_renew')
    # ax1.title('可再生—-不可再生能源图')
    ax1.set_label('Year')
    ax1.set_label('Quantity')
    ax1.tick_params(axis='y')

    ax2=ax1.twinx()
    ax2.plot(x[:-1], renew_growth, label='renew_growth',color='red')
    ax2.plot(x[:-1], nonrenew_growth, label='nonrenew_growth',color='blue')
    ax2.set_ylabel('Growth Rate (%)')
    ax2.tick_params(axis='y')

    plt.title('可再生—-不可再生能源图')
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.xticks(x + bar_width / 2, x)

    # 显示图表
    plt.show()


Energy_handle()