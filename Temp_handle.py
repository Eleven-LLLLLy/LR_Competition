import math

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def data_handle():
    data=pd.read_csv("Data_Source/Temp.csv")
    data=data.loc[:,'F2010':'F2021']
    data=data.values
    for index,i in enumerate(data):
        x = np.where(~np.isnan(i))[0]  # 存储非缺失值下标
        if len(x)*3>len(i):
            # index_del.append(index)
            continue
        y = i[~np.isnan(i)]  # 非缺失值
        if len(y)==0:
            continue
        model = LinearRegression()
        model.fit(x.reshape(-1, 1), y)
        # 填充缺失值
        x_missing = np.where(np.isnan(i))[0]
        y_missing = model.predict(x_missing.reshape(-1, 1))
        i[x_missing] = y_missing
        # 输出填充后的数据
    array = data.tolist()
    for i in array:
        if any(math.isnan(x) for x in i):
            array.remove(i)
    x=list(range(2010,2022))
    y=[val for sublist in array for val in sublist]
    plt.scatter(x*len(array),y, marker='^', s=100, c='green')
    # 设置x轴和y轴的标签
    plt.xlabel('Year')
    plt.ylabel('Rate')
    plt.style.use('ggplot')
    # 显示图形
    plt.show()
def Temp_handle():
    data=pd.read_csv("Data_Source/Temp.csv")
    #ISO2、ISO3、Indicator等数据与本次数据无关则直接清除
    data = data.drop(['ISO2','ISO3','Indicator','Unit','Source','CTS_Code','CTS_Name','CTS_Full_Descriptor'], axis=1)

    grouped = data.groupby('Country/Region')
    World_data = grouped.get_group('World').loc[:,'F2010':'F2021'].sum()
    x = ['F2010', 'F2011', 'F2012', 'F2013', 'F2014', 'F2015', 'F2016', 'F2017', 'F2018', 'F2019', 'F2020', 'F2021']
    plt.plot(x, World_data.values)
    plt.title('Tempchange of F2010-F2021')
    plt.xlabel('Year')
    plt.ylabel('change_rate')
    plt.show()
Temp_handle()
data_handle()