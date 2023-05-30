#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Data_Analyse 
@File    ：Life_Type_handle.py
@IDE     ：PyCharm 
@Author  ：Lsy
@Date    ：2023/5/30 23:17 
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
def handle_singlefile(path):
    #对单个文件处理流程
    data=pd.read_csv(path)
    # data.info()
    #以dwc:taxonID列为基础消除重复值(判定重复值)
    data = data.drop_duplicates(subset=['dwc:taxonID'])
    # data.info()
    #缺失值处理
    null_counts=data.isnull().sum()
    #对所需使用的数据进行缺失值填充
    data['gbif:isExtinct']=data['gbif:isExtinct'].fillna('unknown')
    #统计
    counts=data['gbif:isExtinct'].value_counts()
    percentages=(data['gbif:isExtinct'].value_counts(normalize=True)*100).reset_index()
    percentage=percentages.iloc[2,1]
    return percentage

# 对多个文件进行处理得出图像
def Life_Type_handle():
    folder_path='Data_Source\\Life_type'
    file_names=[f for f in os.listdir(folder_path)]
    #按照年份对文件进行排序
    file_names=sorted(file_names)
    rate=[]
    for file_name in file_names:
        file_path=os.path.join(folder_path,file_name)
        print(file_path)
        temp=handle_singlefile(file_path)
        rate.append(temp)
    years = [2018, 2019, 2020, 2021, 2022]
    # 绘制饼状图
    plt.xlabel('Year')
    plt.ylabel('Extinction Rate (%)')
    plt.pie(rate, labels=years, autopct='%1.1f%%')
    plt.title('Global Extinction Rate (2018-2022)')

    # 显示图形
    plt.show()