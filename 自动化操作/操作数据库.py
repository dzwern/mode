import requests
import time
import csv
import json
from mysql import DZWMysql


# def save_data(df):
#     sql = '''
#     INSERT INTO `ADS_DM_mno_aveMoney_d`
#     (`mno`,`sevenAveMoney`,`lastAveMoney`)
#     VALUES (%s,%s,%s)
#     ON DUPLICATE KEY UPDATE
#         `mno`= VALUES(`mno`),`sevenAveMoney`= VALUES(`sevenAveMoney`),`lastAveMoney`= VALUES(`lastAveMoney`)
#     '''
#     dw_mysql.executeSqlManyByConn(sql, df.values.tolist())

def get_zhihu():
    sql = '''
    SELECT DISTINCT
        times 
    FROM
        zhihu_hot 
    ORDER BY
        times
    '''
    df = zwmysql.get_dataframe_pd(sql)
    return df


def main():
    df_zhihu = get_zhihu()
    print(df_zhihu)


if __name__ == '__main__':
    zwmysql = DZWMysql.ZwMysql('spider')
    main()
