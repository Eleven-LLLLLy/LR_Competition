#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Data_Analyse 
@File    ：Energy_handle.py
@IDE     ：PyCharm 
@Author  ：Lsy
@Date    ：2023/5/29 18:38 
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def Energy_handle():
    plt.rcParams['font.family'] = ['SimHei']
    '''数据处理，针对国家、类型进行分类，并选定特定年份'''
    data=pd.read_csv('Data_Source/Energy_Transition.csv')
    data.info()
    data=data.groupby('Country/Region')
    data=data.get_group('World')
    '''使用Electricity Generation实际电力量进行计算'''
    data =data.groupby('Indicator')
    data = data.get_group('Electricity Installed Capacity')
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