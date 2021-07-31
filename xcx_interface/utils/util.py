'''
# 作者：林景恒
# 时间：20200612
# 描述：工具函数、工具类
'''

import requests
import json
import datetime
# from datetime import datetime
from django.db import connection  # transaction


class HttpRequest(object):
    '''
    用于发起 http GET 和 POST 请求
    '''
    @classmethod
    def request(cls, method, url, data=None, headers=None):
        method = method.upper()
        if method == 'POST':
            return requests.post(url=url, data=data, headers=headers)
        elif method == 'GET':
            return requests.get(url=url, params=data, headers=headers)


def convertDic(data):
    '''
    将数据转为字典数据
    Args:
        data: 字典数据。
    '''
    # 转为 JSON 对象
    json_str = json.dumps(data)
    # JSON 对象类型转换为 Python 字典
    json_dic = json.loads(json_str)
    return json_dic


def convertJson(data, ascii=False):
    '''
    将数据转为 JSON 对象
    Args:
        data: 字典数据。
        ascii: 是否启用 ASCII 编码。
    '''
    json_str = json.dumps(data, cls=DateEncoder)
    return json_str


def convertJsonAscii(data, ascii):
    json_str = json.dumps(data, ensure_ascii=ascii)
    return json_str


def tick():
    '''
    时间打印
    '''
    print('Tick! The time is: %s' % datetime.datetime.now())


def resSuccess(data):
    '''
    成功响应
    Args:
        data: 数据。
    '''
    res = {
        "code": 200,
        "data": data,
        "msg": 'success'
    }
    return res


def resError(data):
    '''
    错误响应
    Args:
        data: 数据。
    '''
    res = {
        "code": -1,
        "data": '',
        "msg": data
    }
    return res


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        '''
        datetime 转换成 JSON 特殊处理
        '''
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')

        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")

        else:
            return json.JSONEncoder.default(self, obj)


def executeSelect(sql, isOnlyRow=True):
    '''
    执行 SELECT 语句
    Args:
        sql: SQL语句。
        isOnlyRow: 是否返回一条记录,True 是，False 否。
    '''
    cursor = connection.cursor()
    cursor.execute(sql)
    if isOnlyRow:
        row = cursor.fetchone()
    else:
        row = cursor.fetchall()
    if len(row) == 0:
        return []
    else:
        return rowMapField(row, cursor)


def getProcedure(procName, params):
    '''
    调用存储过程
    Args:
        procName: { string } 存储过程名
        params: { tuple } 传入存储过程中的参数
    '''
    cursor = connection.cursor()
    cursor.callproc(procName, params)
    connection.connection.commit()
    result = cursor.fetchall()
    if len(result) == 0:
        return []
    else:
        return rowMapField(result, cursor)


def tableFieldHandle(cursor):
    '''
    表字段映射元组数据
    Args:
        cursor：游标。
    '''
    SqlDomain = cursor.description
    DomainNum = len(SqlDomain)
    SqlDomainName = [None] * DomainNum if DomainNum > 0 else []
    for i in range(DomainNum):
        SqlDomainName[i] = SqlDomain[i][0]
    return SqlDomainName


def rowMapField(row, cursor):
    '''
    表头字段和值的映射
    Args:
        row: 执行SQL查询出的数据。
        cursor: 游标。
    '''
    fieldTuple = tableFieldHandle(cursor)
    dataTupleNum = len(row)
    dataTupleList = [None] * dataTupleNum if dataTupleNum > 0 else []
    for i in range(dataTupleNum):
        obj = {}
        for j in range(len(fieldTuple)):
            obj[fieldTuple[j]] = row[i][j]
        dataTupleList[i] = obj
    cursor.close()
    return dataTupleList
