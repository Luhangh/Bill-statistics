# -*- coding: utf-8 -*-

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.font_manager import FontProperties   #显示中文，并指定字体




# 按商家分类
def group_pieChart(saveName,chartObj):
    data = pd.Series(chartObj)
    #print(data)
    myfont=FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc',size=14)
    sns.set(font=myfont.get_name())

    plt.rcParams['figure.figsize'] = (8.0, 6.0)   #调整图片大小

    lbs= data.index
    explodes=[0.1 if i=='其他' else 0 for i in lbs]
    plt.pie(data, explode=explodes,labels=lbs, autopct="%1.1f%%",
                                    colors=sns.color_palette("muted"),startangle = 90,pctdistance = 0.6,
            textprops={'fontsize':14,'color':'black'})


    plt.axis('equal')  # 设置x，y轴刻度一致，以使饼图成为圆形。
    plt.savefig('./images/'+saveName+'.jpg')
    plt.show()

# 堆积柱状图分类
def group_histogram(saveName,index,chartObj,columns):
    # data = pd.Series(chartObj)
    bean = [[1, 2, 3], 
                    [2, 3, 4],
                    [3, 4, 5]]
    data = pd.DataFrame(chartObj, columns=columns,
                   index=index)
    myfont=FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc',size=14)
    sns.set(font=myfont.get_name())
    plt.rcParams['figure.figsize'] = (8.0, 6.0)   #调整图片大小
    plt.rcParams['axes.unicode_minus']=False      #显示负号
    #pal_style = ['deep', 'muted', 'pastel', 'bright', 'dark','colorblind']
    sns.set_palette(sns.color_palette('bright'))  #设置调色板
    data.plot.bar(stacked=True, alpha=0.5, )   

    plt.xticks(fontsize=16, rotation=0)    #设置x和y轴刻度值的字体大小;rotation规定水平排列刻度文字。
    plt.xticks(fontsize=16)    #设置x轴刻度值的字体大小
    plt.yticks(fontsize=16)    #设置y轴刻度值的字体大小

    plt.legend(fontsize=16)    #设置legend刻度值的字体大小
    plt.title="支付宝历年账单收支堆积柱状图"
    plt.yticks(np.arange(0, 350000, 20000)) #设置y轴标签
    plt.savefig('./images/'+saveName+'.jpg')
    plt.show()