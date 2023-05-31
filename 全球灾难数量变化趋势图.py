# -*- coding:utf-8 -*-
"""
作者：ruanwh
日期：2023年05月16日
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['SimHei']

np.set_printoptions(suppress=True,   precision=20,  threshold=10,  linewidth=40) #控制python中小数的精度 #np禁止科学计数法显示
pd.set_option('display.float_format',lambda x : '%.2f' %x) #设置数据的最大显示行数和列数，显示小数位数为两位 #pd禁止科学计数法显示

data = pd.read_csv(r'C:\Users\ASUS\Desktop\数据集\全球自然灾害数据\Disaster.csv') # 读取数据

#去重处理
data.drop_duplicates(inplace=True) # 使用drop_duplicates去重，inplace=True对原数据集进行替换
data.reset_index(drop=True, inplace=True) # 删除数据后，恢复索引

# data.info()

def filter_col_by_nan(data, narate=0.2):#删除缺失值在20%以上的变量
    n_samples = data.shape[0]
    list_nan_cols = []
    for col in data.columns:
        if data[col].isna().sum() / n_samples >= (narate):
            list_nan_cols.append(col)

    print(f'缺失量在{narate * 100}%以上的变量有:{list_nan_cols}')
    return list_nan_cols

#删除缺失值过高的变量
list_nullfactor_todrop = filter_col_by_nan(data, narate=0.2)
data = data.drop(list_nullfactor_todrop, axis=1).copy()
# print(data.keys())


group=data.groupby("Year")#取年份分组
print(group.size())
subset = group.size().tolist()[10:22]#将size()统计后的数据转换为列表并取11行到21行
print(subset)
x= np.array(['2010','2011','2012','2013','2014','2015',
             '2016','2017','2018','2019','2020','2021'])#取2010-2021的数据
y = np.array(subset)

plt.plot(x, y)
plt.xlabel('年份')
plt.ylabel('总频次')
plt.title('2010-2021全球灾难数量变化趋势图')

plt.show()



