# -*- coding: utf-8 -*-
# 616566709@qq.com haotin
# 2016-05-26

import pymongo
import pandas as pd
import cx_Oracle
pd.set_option('display.width', 350)
"""
:param: get from mongodb
:param: to mongodb
:param get from oracle
:param to oracle
:return:
"""
def GetDataFromMongo():
    client = pymongo.MongoClient('192.168.10.252' , 27017)
    db_name = 'alpha_factor'
    db = client.alpha_factor
    collection = db.alpha_factor

    a = collection.find({"CODE" : 600653,"TRADEDATE" :20160930})
    # find条件({"type": '1440min',"id": '150019_sz',"st" : {$gte:ISODate("2016-09-18T16:00:00.000Z")},"et" : {$lte:ISODate("2016-09-19T07:00:03.000Z")}})
    a = list(a)
    data = pd.DataFrame(a)
    # print data
    return data

    # dbClient = pymongo.MongoClient(host, port)
    # collection = dbClient['stocks']['alpha_factor']

def ToMongo(df):
    client = pymongo.MongoClient('192.168.10.252' , 27017)
    db_name = 'alpha_factor'
    db = client.alpha_factor
    collection = db.alpha_factor

    df = df.to_dict(orient="records")
    collection.insert_many(df)


def GetStockdailyWind():

    conn=cx_Oracle.connect('system/dhhx1234@192.168.10.95/wind')
    curs=conn.cursor()

    selectsql = "select b.f1_0001,a.f2_1425,a.f4_1425,a.f5_1425,a.f6_1425,a.f7_1425,a.f8_1425,\
    a.f9_1425,a.f10_1425 from tb_object_1425 a left join tb_object_0001 b on a.f1_1425 = b.f16_0001 where \
    b.F10_0001 = '100001000' and b.F12_0001 = 'A' and a.f2_1425 >'20060630' ORDER BY b.f1_0001,a.F2_1425"
    curs.execute(selectsql)

    a = curs.fetchall()
    df = pd.DataFrame(a)
    df.columns = ['code','date','o','h','l','c','v','a','w']
    for code in set(df['code']):

        data = df[df['code']==code]
        if len(data.keys()) ==9 and data.shape[0]>0:
            print code

            weight = data.iloc[-1,8]
            data['o'] = data['o']/weight
            data['h'] = data['h']/weight
            data['l'] = data['l']/weight
            data['c'] = data['c']/weight
            data['v'] = data['v']*100
            data['a'] = data['a']*1000
            data = data[data['v'] != 0]
            data = data[['date','o','h','l','c','v','a']]
            # print data
            data.to_csv('D:/data/stock_daily_wind_csv/'+code[7:9]+code[:6]+'.txt',index=False,header=False,sep='\t',float_format='%.4f')

        else:
            pass


if __name__ == "__main__":
    df = GetDataFromMongo()
    # ToMongo(df)
    # GetStockdailyWind()