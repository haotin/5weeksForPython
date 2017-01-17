# -*- coding: utf-8 -*-
"""
@author: Xing
"""
import pandas as pd

# =====导入数据
df = pd.read_csv('sz300001.csv', encoding='gbk')
# print df
# 导入后发现是乱码，加上encoding='gbk'参数

# print df['股票代码']  # 发现有问题，报错
print df.columns[0], type(df.columns[0])
# print df[u'股票代码']  # encoding之后所有的字符串都变成了unicode格式
df.columns = [i.encode('utf8') for i in df.columns]  # 每次打u太麻烦，将unicode再变成string
print df.columns[0], type(df.columns[0])

# 取我们需要的列，其他的列不要
df = df[['交易日期', '股票代码', '开盘价', '最高价', '最低价', '收盘价', '涨跌幅']]
# 将数据按照交易日期从小到大排序
df.sort_values(by=['交易日期'], inplace=True)

# =====计算复权价，最重要的就是涨跌幅要复权。下面考察我们的数据中的涨跌幅
df['涨跌幅2'] = df['收盘价'].pct_change()  # 通过pct_change计算基于未复权收盘价的涨跌幅
print df[abs(df['涨跌幅2'] - df['涨跌幅']) > 0.0001]  # 数据中的涨跌幅是复权后的涨跌幅
del df['涨跌幅2']

# =====计算复权后的授权价
# ===计算复权因子
df['复权因子'] = (df['涨跌幅'] + 1).cumprod()
# 计算出来的复权因子的意义：我在一开始投入1元买这个股票，最后的收益是多少，资金曲线是什么样子的。
# 如果要计算投入100万买入这个股票，资金曲线是什么样子的，df['复权因子'] * 100万即可

# ===后复权收盘价，等于用等于该股票上市价格的钱，买入该股票后的资金曲线。
initial_price = df.iloc[0]['收盘价'] / (1 + df.iloc[0]['涨跌幅'])  # 计算上市价格
df['收盘价_后复权'] = initial_price * df['复权因子']  # 相乘得到复权价

# ===如果计算复权的开盘价、最高价、最低价？
# 根据如下公式计算：'开盘价_复权' / '收盘价_复权' = '开盘价' / '收盘价'
df['开盘价_后复权'] = df['开盘价'] / df['收盘价'] * df['收盘价_后复权']
df['最高价_后复权'] = df['最高价'] / df['收盘价'] * df['收盘价_后复权']
df['最低价_后复权'] = df['最低价'] / df['收盘价'] * df['收盘价_后复权']
print df

# ===计算前复权价格
# 作为本周作业

# =====导出数据
df.to_csv('output_fuquan_sz300001.csv')
df.to_csv('output_fuquan_sz300001.csv', index=False,
          mode='w',  # mode='w'代表覆盖之前的文件，mode='a'，代表接在原来数据的末尾
          float_format='%.15f',  # 控制输出浮点数的精度
          header=None,  # 不输出表头
          )
