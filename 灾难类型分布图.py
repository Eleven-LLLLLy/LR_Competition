# -*- coding:utf-8 -*-
"""
作者：ruanwh
日期：2023年05月30日
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


group=data.groupby("Disaster Type")#自然灾害类型分组
print(group.size())
head=group.size().keys()#灾难种类
print(head)
subset = group.size().values#每种灾难数量
print(subset)
typenum = group.size().keys().size#灾难种数
DisasterSum = group.size().sum()#总灾难数
print(DisasterSum)
list1=[]
list2=[]
for i in range(0,typenum):#进行筛选，占比大于0.1%的灾难才画图
    if subset[i] / DisasterSum>=0.001:
        list1.append(head[i])
        list2.append(subset[i])

print(list1)
print(list2)
labels=np.array(list1)
sizes=np.array(list2)
# plt.pie(sizes,labels=labels,autopct='%1.1f%%')
fig, ax = plt.subplots()

colors = ["#FFC0CB", "#FFA07A", "#FF8C00", "#FFD700", "#ADFF2F", "#FF69B4", "#D2B48C",
          "#7FFFD4", "#FFE4B5", "#E6E6FA", "#FFB6C1"]
# 绘制环状饼状图
wedges, texts, autotexts = ax.pie(sizes, autopct='%1.1f%%', startangle=90, counterclock=False,
                                  wedgeprops={'width': 0.6}, textprops={'fontsize': 12},
                                  labels=labels, pctdistance=0.8, labeldistance=1.1,colors=colors)

# 设置中心圆形
centre_circle = plt.Circle((0, 0), 0.5, fc='white')
ax.add_artist(centre_circle)


plt.title('全球灾难类型统计图')
plt.show()