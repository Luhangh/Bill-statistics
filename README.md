# 统计下自己的历年账单  花出去了多少钱
图表可视化统计微信和支付宝的账单，看看自己历年花了多少钱
## 账单准备
先去[支付宝网页版](https://consumeprod.alipay.com/record/advanced.htm)，按自定义时间下载你一年的支付宝账单。      
微信的账单比较麻烦，要去支付>钱包>账单里面导出，一次只能导出3个月，一年的账单需要分4多次导出。
支付宝的账单默认是gbk编码，需要另存为csv utf-8编码    
最后把这些csv文件放到这个项目的csv文件夹    

## 配置config
修改config.py里面的文件名为你的账单文件名,如下：
```python
alipay_list = ["alipay.csv"]
wechatpay_list = [
    "wechat20180101-20180401.csv",
    "wechat20180401-20180701.csv",
    "wechat20180701-20181001.csv",
    "wechat20181001-20190101.csv",
]
```
## 使用

#### 图表中文字体配置

```python
#mac下指定中文字体路径
fname = "/System/Library/Fonts/STHeiti Light.ttc"
#windows下： 第一步：将项目font文件夹下中文字体Simhei复制到C:/Windows/Fonts的字体目录中
# fname = "C:/Windows/Fonts/simhei.ttf"
```

执行脚本主逻辑在main.py
```python
if __name__ == '__main__':
    # 初始化一下输出文件的环境
    # 默认把结果写到result/result.txt
    # 你可以用file_init('a.txt')改变输出文件名
    file_init()
    # 读取config配置的csv文件
    read_file(data_list)

```

####控制台输出
```python
功能列表：   
 0.全部账单统计                                                                             
 1.支付宝交易类型饼状图
 2.微信交易类型饼状图
 11.支付宝年度账单统计
 12.支付宝历年账单收支堆积柱状图
```
