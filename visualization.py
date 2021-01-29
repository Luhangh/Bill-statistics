# -*- coding: utf-8 -*-

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd



# 按商家分类
def group_pieChart(saveName,chartObj):
    data = pd.Series(chartObj)
    #print(data)

    from matplotlib.font_manager import FontProperties   #显示中文，并指定字体
    myfont=FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc',size=14)
    sns.set(font=myfont.get_name())

    plt.rcParams['figure.figsize'] = (8.0, 6.0)   #调整图片大小

    lbs= data.index
    explodes=[0.1 if i=='其他' else 0 for i in lbs]
    plt.pie(data, explode=explodes,labels=lbs, autopct="%1.1f%%",
                                    colors=sns.color_palette("muted"),startangle = 90,pctdistance = 0.6,
            textprops={'fontsize':14,'color':'black'})


    plt.axis('equal')  # 设置x，y轴刻度一致，以使饼图成为圆形。
    plt.savefig(saveName+'.jpg')
    plt.show()