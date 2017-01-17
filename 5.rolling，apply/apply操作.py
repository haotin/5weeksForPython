# -*- coding: utf-8 -*-
"""
@author: Xing
"""
import pandas as pd
import Functions
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行

# 读入数据
code = 'sz300001'
df = Functions.import_stock_data(code)
print df

# 使用apply方法，apply的参数是函数名
# 定义几个简单的函数，演示apply
def f1(x):
    return x*100
    # return max(x)
    # 可以是比较复杂的操作
    # 我可以进行哪些操作？看看x是什么？
    # print x
    # print type(x)
    # exit()
print df[['收盘价']].apply(f1)

# lambda函数定义方法
# 通常用于定义一些比较简单的、一次性的、一行代码可以解决的函数
print df['收盘价'].apply(lambda x: x*100)

# apply、lambda是较高级的应用，大家一开始不用强行使用。之后看的多了自然也就理解会用了