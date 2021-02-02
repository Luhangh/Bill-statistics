# -*- coding: utf-8 -*-
import csv
import re
import time
import pandas as pd
import os

from config import alipay_list, wechatpay_list


#创建一个空列表，存储当前目录下的CSV文件全称
file_name = []

#type 1支付宝 2微信 0 全部
def read_file(type,data_list):
    read_filename()
    if(1 == type):
       read_afile(data_list)
    elif (2 == type):
        read_wfile(data_list)
    else:
        read_wfile(data_list)
        read_afile(data_list)


def read_filename():
    #将指定目录下的所有文件名称读取进来
    a = os.listdir('csv')
    for j in a:
    #判断是否为CSV文件，如果是则存储到列表中
        if os.path.splitext(j)[1] == '.csv':
            file_name.append(j)


def read_afile(data_list):
    for file in file_name:
        if 'alipay_record' in file:
            read_alipay_file('./csv/' + file, data_list)
#读取指定文件列表
def read_wfile(data_list):
    for file in file_name:
         if '微信支付' in file:
            read_wechatpay_file('./csv/' + file, data_list)
#读取指定文件
def read_wfile_one(data_list):
        read_wechatpay_file('./csv/' + '微信支付账单(20190205-20190505).csv', data_list)

def read_alipay_file(file_name, data_list):
    start = False
    # f = codecs.open(file_name, 'wb', "gbk")
    csv_reader = csv.reader(open(file_name))
    # csv_reader =  csv_1_xlsx(file_name)
    for row in csv_reader:
        if re.search('交易号', row[0]):
            start = True
            continue
        elif re.search('--------------------------', row[0]) and start:
            break
        if start:
            try:
                date = time.strptime(row[2].strip(), "%Y-%m-%d %H:%M:%S")
            except:
                date = time.strptime(row[2].strip(), "%Y/%m/%d %H:%M")
            data = {
                "pay_num": float(row[9]),
                "pay_type": '',
                "pay_time": date,
                "pay_object": row[7].strip(),
                'id': row[0],
                'trade_type':row[5],
                'pay_pro':row[8],
                'pay_way':'',
                'pay_state':row[11],
                'merchants_no':row[1].strip('\t'),
            }
            if re.search('支出', row[10]):
                data['pay_type'] = '支出'
            elif re.search('收入', row[10]):
                data['pay_type'] = '收入'
            else:
                if re.search('已收入',row[15]):
                  data['pay_type'] = '收入'
                elif re.search('已支出',row[15]):  
                  data['pay_type'] = '支出' 
                else:
                    continue
                continue                
            data_list.append(data)
    print(file_name + "读取完成")


def read_wechatpay_file(file_name, data_list):
    start = False
    csv_reader = csv.reader(open(file_name))
    for row in csv_reader:
        if re.search('交易时间', row[0]):
            start = True
            continue
        if start:
            try:
                data = {
                "pay_num": float(row[5].strip('¥')),
                "pay_type": '',
                "pay_time": time.strptime(row[0], "%Y-%m-%d %H:%M:%S"),
                "pay_object": row[2].strip() if row[2] != '/' else row[1].strip(),
                'id': row[8].strip('\t'),
                'trade_type':row[1],
                'pay_pro':row[3],
                'pay_way':row[6],
                'pay_state':row[7],
                'merchants_no':row[9].strip('\t'),
              }
            except ValueError:
                    data['pay_num'] = float(row[6].strip('¥'))
            
            if re.search('支出', row[4]):
                data['pay_type'] = '支出'
            elif re.search('收入', row[4]):
                data['pay_type'] = '收入'
            else:
                if row[7] in '支付成功':
                     data['pay_type'] = '支出'

            data_list.append(data)
    print(file_name + "读取长度"+str(len(data_list)))


def csv_2_xlsx(srcPath):
    try:
        data = pd.DataFrame(pd.read_csv(srcPath, encoding='utf8', low_memory=False))
    except:
        data = pd.DataFrame(pd.read_csv(srcPath, encoding='gbk', low_memory=False))
    data.to_excel(srcPath[:-3] + 'xlsx', sheet_name='Sheet1', index=False)
    
