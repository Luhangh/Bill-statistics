# -*- coding: utf-8 -*-
from os import fork
from read_file import read_file
from write_file import file_init
from statistics import *
from visualization import *
import matplotlib.pyplot as plt
import pandas as pd
import time
import datetime
from config import *

data_list = []
'''
data_list= [data1, data2, data3]
data = {
    "pay_num": 0.0,
    "pay_type": '',
    "pay_time": '',
    "pay_object": '',
    'trade_type':row[1],
    'pay_pro':row[3],
    'pay_way':row[6],
    'pay_state':row[7],
    'merchants_no':row[9].strip('\t'),
}
'''


if __name__ == '__main__':
    # 初始化一下输出文件的环境
    # 默认把结果写到result/result.txt
    # 你可以用file_init('a.txt')改变输出文件名
    file_init()
    # 读取config配置的csv文件
    
    read_file(groupType,data_list)
    t = int(time.time())
    if groupType == 2:
        obj = group_typeChart(wx_types,'trade_type',data_list)
        group_pieChart("微信交易类型饼状图",obj)
    elif groupType == 1:
        obj = group_typeChart(alipay_types,'pay_object',data_list)
        group_pieChart("支付宝交易类型饼状图",obj)
    elif groupType == 11:
        objTime = group_timeChart(time_types,data_list)
        group_pieChart("支付宝交易时间段饼状图",objTime)
    
    
    






    # 简单的统计
    # count(data_list)
    # # 统计50~100的消费和收入
    # select_cost_between(50, 100, data_list)
    # # 只统计50~100的消费
    # select_cost_between(50, 100, data_list, pay_only=True)
    # # 统计在某些商家上的消费
    # spend_on_seller('M29超市', data_list)
    # spend_on_seller('i校长', data_list)
    # spend_on_seller('洋洋洋', data_list)
    # spend_on_seller('河南正商物业管理有限公司', data_list)
    # spend_on_seller('发出群红包', data_list)
    # # 按照支付对象分类统计，从小到大排序，正数为输出，负数为收入
    # group_by_seller(data_list)
    # t1= group_by_type('商户消费', data_list)
    # t2=group_by_type('零钱提现', data_list)
    # t3 =group_by_type('微信红包', data_list)
    # t4=group_by_type('转账', data_list)