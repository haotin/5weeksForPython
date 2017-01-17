# -*- coding: utf-8 -*-
"""
@author: xingbuxing
汇总常用函数
"""
import pandas as pd  # 导入pandas，我们一般为pandas去一个别名叫做pd


# 导入数据
def import_stock_data(stock_code):
    """
    导入股票数据，股票数据必须与程序处于同一文件路径。
    只导入如下字段：'交易日期', '股票代码', '开盘价', '最高价', '最低价', '收盘价', '涨跌幅', '成交量'
    最终输出结果按照日期排序
    :param stock_code:
    :return:
    """
    df = pd.read_csv(stock_code+'.csv', encoding='gbk')
    df.columns = [i.encode('utf8') for i in df.columns]
    df = df[['交易日期', '股票代码', '开盘价', '最高价', '最低价', '收盘价', '涨跌幅', '成交量']]
    df.sort_values(by=['交易日期'], inplace=True)
    df['交易日期'] = pd.to_datetime(df['交易日期'])
    df.reset_index(inplace=True, drop=True)

    return df


# 计算复权价
def cal_fuquan_price(input_stock_data, fuquan_type='后复权'):
    # copy输入的数据
    df = input_stock_data.copy()

    # 判断输入数据中是否包含计算复权价格所需要的字段
    # col_list = df.columns
    # for i in ['开盘价', '最高价', '最低价', '收盘价', '涨跌幅', 'a']:
    #     if i not in col_list:
    #         raise '数据中不包含收盘价'

    # 计算复权收盘价
    num = {'后复权': 0, '前复权': -1}
    price1 = df['收盘价'].iloc[num[fuquan_type]]
    df['复权因子'] = (1.0+df['涨跌幅']).cumprod()
    price2 = df['复权因子'].iloc[num[fuquan_type]]
    df['收盘价_'+fuquan_type] = df['复权因子'] * (price1 / price2)

    # 计算复权的开盘价、最高价、最低价
    df['开盘价_'+fuquan_type] = df['开盘价'] / df['收盘价'] * df['收盘价_'+fuquan_type]
    df['最高价_'+fuquan_type] = df['最高价'] / df['收盘价'] * df['收盘价_'+fuquan_type]
    df['最低价_'+fuquan_type] = df['最低价'] / df['收盘价'] * df['收盘价_'+fuquan_type]

    return df[[i+'_'+fuquan_type for i in '开盘价', '最高价', '最低价', '收盘价']]
