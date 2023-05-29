import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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