# -*- coding: utf-8 -*-
"""
@author: xingbuxing
汇总所有信号产生函数
"""


def signal_ma(df, ma_short=5, ma_long=20):
    """
    均线策略：
    当短期均线由下向上穿过长期均线的时候，第二天以开盘价全仓买入并在之后一直持有股票。
    当短期均线由上向下穿过长期均线的时候，第二天以开盘价卖出全部股票并在之后一直空仓，直到下一次买入。

    :param df:
    :param ma_short: 短期均线
    :param ma_long: 长期均线
    :return:
    """

    # ===计算均线
    df['ma_short'] = df['收盘价'].rolling(ma_short, min_periods=1).mean()
    df['ma_long'] = df['收盘价'].rolling(ma_long, min_periods=1).mean()

    # ===找出买入信号
    # 当天的短期均线大于等于长期均线
    condition1 = (df['ma_short'] >= df['ma_long'])
    # 上个交易日的短期均线小于长期均线
    condition2 = (df['ma_short'].shift(1) < df['ma_long'].shift(1))
    # 将买入信号当天的signal设置为1
    df.loc[condition1 & condition2, 'signal'] = 1

    # ===找出卖出信号
    # 当天的短期均线小于等于长期均线
    condition1 = (df['ma_short'] <= df['ma_long'])
    # 上个交易日的短期均线大于长期均线
    condition2 = (df['ma_short'].shift(1) > df['ma_long'].shift(1))
    # 将买入信号当天的signal设置为0
    df.loc[condition1 & condition2, 'signal'] = 0

    # 将无关的变量删除
    df.drop(['ma_short', 'ma_long'], axis=1, inplace=True)

    return df
