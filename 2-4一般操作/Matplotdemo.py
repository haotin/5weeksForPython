# -*- coding: utf-8 -*-
#616566709@qq.com _author_haotin
#2016-01-26

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import sqlalchemy as sa
import tushare as ts
from math import sqrt
import seaborn # 画图美化
pd.set_option('display.width', 350)

# =================================================================

df=ts.get_hist_data('150153',start='2016-05-26',end='2016-08-30')

df.index = map(lambda x: x.replace('-', ''), df.index)
df['date']=df.index
df.sort_values(by='date',inplace=True)




df['p_change'].plot(figsize=(12,5))         # 折线图
plt.show()
plt.xlabel('date')
plt.ylabel('p_change')
plt.title('WEEK_CHANGE')
# plt.text(1,1,'hehe')
# plt.savefig('C:/Users/Administrator/Desktop/glp.png', dpi = 75)

df['p_change'].plot.hist(figsize=(12,5))    # 柱状图
plt.show()



