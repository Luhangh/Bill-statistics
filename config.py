# -*- coding: utf-8 -*-

alipay_list = ['alipay_record_20210128_1549_1.csv']
wechatpay_list = [
    "微信支付账单(20201129-20210128).csv",
    # "wechat20180401-20180701.csv",
    # "wechat20180701-20181001.csv",
    # "wechat20181001-20190101.csv",
]

# alipay_types = ['支付宝网站','淘宝','其他（包括阿里巴巴和外部商家）']
wx_types = ['商户消费','零钱提现','微信红包','转账']

alipay_types = ['哈啰出行','长信基金管理有限责任公司','蚂蚁会员（北京）网络技术服务有限公司']

time_types=['2015年','2016年','2017年','2018年','2019年','2020年','2021年']

types = [wx_types,alipay_types,time_types,
        ["收入","支出"]]

#0全部 ，1 支付宝， 2微信
groupType = 1