import sys
import traceback
import decimal
import pandas as pd
from sqlalchemy import create_engine
from itertools import cycle

'''
连接数据库的两种方式
（1）使用pymysql直接连
（2）使用SQLalchemy连

'''

# 创建连接的数据库
# db = pymysql.connect(host='localhost', port=3306, user='root', password='021412', db='spider',
#                      charset='utf8')
# 填写链接信息
# engine = create_engine("mysql+pymysql://【此处填用户名】:【此处填密码】@【此处填host】:【此处填port】/【此处填数据库的名称】?charset=utf8")
# url='mysql+pymysql://root:021412@localhost:3306/spider/?charset=utf8mb4'


url = 'mysql+pymysql://root:021412@localhost:3306/'


# 创建类
class ZwMysql(object):
    # 初始化
    def __init__(self, schema='spider'):
        self._engin = create_engine(url + schema + '?charset=utf8mb4', pool_pre_ping=True, pool_recycle=3600 * 4)
        self.schema = schema

    # 连接池的状态
    def getpoolstatus(self):
        return self._engin.pool.status()

    # 获取连接
    def getconnection(self):
        conn = self._engin.connect()
        return conn

    # 释放连接
    def closeconnection(self, conn):
        if conn:
            conn.close()

    # 执行SQL
    def executesqlbyengine(self, sql='select * from DUAL'):
        return self._engin.execute(sql)

    # 执行SQL
    def executesqlbyconn(self, sql='SELECT * FROM DUAL', conn=None):
        conn = conn or self.getconnection()
        with conn as connection:
            return connection.execute(sql)

    # 批量执行更新SQL语句
    def excutesqlmanybyconn(self, sql='', data=[], conn=None):
        if len(data) > 0:
            conn = conn or self.getconnection()
            with conn as connection:
                return connection.execute(sql, data)

    # 加载数据到df
    def get_dataframe_pd(self, sql='select * from dual', conn=None):
        conn = conn or self.getconnection()
        with conn as connection:
            dataframe = pd.read_sql(sql, connection)
            return dataframe

    # 保存df到数据库
    def save_dataframe_pd(self, pd, table, conn=None):
        conn = conn or self.getconnection()
        with conn as connection:
            pd.to_sql(table, connection, if_exists='append', index=False)

    # 返回结果为列表
    def get_list(self, sql='SELECT * FROM DUAL'):
        result = self._engin.execute(sql)
        result_list = []
        for i in result:
            result_list.append(i[0])
        return result_list


if __name__ == '__main__':
    ZwMysql = ZwMysql()
