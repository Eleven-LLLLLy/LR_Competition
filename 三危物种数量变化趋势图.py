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

data1 = pd.read_csv(r"C:\Users\ASUS\Desktop\数据集\濒危物种数量的变化数据\Critically Endangered.csv") # 极危物种
data2 = pd.read_csv(r"C:\Users\ASUS\Desktop\数据集\濒危物种数量的变化数据\Endangered.csv")    #濒危物种
data3 = pd.read_csv(r"C:\Users\ASUS\Desktop\数据集\濒危物种数量的变化数据\Vulnerable.csv")  #易危物种
#去重处理
data1.drop_duplicates(inplace=True) # 使用drop_duplicates去重，inplace=True对原数据集进行替换
data1.reset_index(drop=True, inplace=True) # 删除数据后，恢复索引
data2.drop_duplicates(inplace=True)
data2.reset_index(drop=True, inplace=True)
data3.drop_duplicates(inplace=True)
data3.reset_index(drop=True, inplace=True)


group=data1.groupby("Year")#取年份分组
x=group.size().keys()
print(x)

group1=data1.groupby("TOTAL")
group2=data2.groupby("TOTAL",sort=False)
group3=data3.groupby("TOTAL",sort=False)

num1=group1.size().keys()
num2=group2.size().keys()
num3=group3.size().keys()

y1=[]
y2=[]
y3=[]

s=''
for i in range(0,22):#数据集内用的是逗号分位数字，将其转换为整型
    for j in range(0,len(num1[i])):
        if num1[i][j]!=',':
            s=s+num1[i][j]
    y1.append(int(s))
    s=''
for i in range(0,22):#数据集内用的是逗号分位数字，将其转换为整型
    for j in range(0,len(num2[i])):
        if num2[i][j]!=',':
            s=s+num2[i][j]
    y2.append(int(s))
    s=''
y2.reverse()
for i in range(0,22):#数据集内用的是逗号分位数字，将其转换为整型
    for j in range(0,len(num3[i])):
        if num3[i][j]!=',':
            s=s+num3[i][j]
    y3.append(int(s))
    s=''
y3.reverse()
print(y1)
print(y2)
print(y3)

fig, ax = plt.subplots()
ax.plot(x, y1, label='Critically Endangered')
ax.plot(x, y2, label='Endangered')
ax.plot(x ,y3,label='Vulnerable')
# ax2=ax.twinx()
# ax2.plot(s, y3, label='Vulnerable')
y=[]
for i in range(0,22):
    y.append(800*(i+1))
plt.yticks(y)

plt.tick_params(axis='x', labelsize=8)
for i in range(len(x)):
    plt.text(x[i], y1[i], y1[i], ha='center', va='bottom')
    plt.text(x[i], y2[i], y2[i], ha='center', va='bottom')
    plt.text(x[i], y3[i], y3[i], ha='center', va='bottom')

ax.legend(loc='upper left')
# ax2.legend(loc='upper right')

plt.xlabel('年份')
plt.ylabel('种类数')
plt.title('三类濒危物种变化趋势图')

plt.show()


