"""
@Author 林景恒
@Date 20200719
@LastModifyDate --
@Desc 系统相关业务
"""
import json
from django.http import HttpResponse
from xcx_interface.utils.util import getProcedure, resSuccess, resError, convertJson


def getInterfaceList(request):
    '''
    接口权限表相关操作
    Args:
        l_type: 0 -查询、1 -插入、2 -更新、3 -删除
    '''
    try:
        params = json.loads(request.body)
        if params['l_uid'] is None:
            raise TypeError('用户ID不能为空')
        dataList = [None] * 11
        dataList[0] = params['l_type']
        dataList[1] = params['l_uid']
        if params['l_type'] == 0:
            if params['vc_shopid'] is not None:
                dataList[2] = params['vc_shopid']
            if params['vc_fmoduleid'] is not None:
                dataList[3] = params['vc_fmoduleid']
        if params['l_type'] == 1 or params['l_type'] == 2:
            childModuleId = None if params['vc_cmoduleid'] == '' else params['vc_cmoduleid']
            interfaceId = None if params['vc_interfaceid'] == '' else params['vc_interfaceid']
            dataList = [params['l_type'], params['l_uid'], params['vc_shopid'], interfaceId, params['vc_fmoduleid'],
                        params['vc_fmodulename'], childModuleId, params['vc_cmodulename'],
                        params['vc_interface'], params['vc_node_interface'], params['vc_interface_desc']]
        if params['l_type'] == 3:
            dataList[3] = params['vc_interfaceid']
        print(tuple(dataList))
        result = getProcedure('InterfaceProc', tuple(dataList))
        res = resSuccess(result)
        return HttpResponse(convertJson(res, False))
    except Exception as e:
        # return HttpResponse(convertJsonAscii(resError(str(e)), False))
        return HttpResponse(convertJson(resError(str(e)), False))


def getUserInfo(request):
    '''
    获取用户信息
    '''
    try:
        params = json.loads(request.body)
        userName = params['username']
        if userName is None:
            raise TypeError('账号不能为空')
        result = getProcedure('UserInfo', (0, userName, None, None, None))
        res = resSuccess(result)
        return HttpResponse(convertJson(res, False))
    except Exception as e:
        # return HttpResponse(convertJsonAscii(resError(str(e)), False))
        return HttpResponse(convertJson(resError(str(e)), False))


def addUserToBlackList(request):
    '''
    将用户添加到黑名单
    '''
    try:
        params = json.loads(request.body)
        if params['l_uid'] is None:
            raise TypeError('用户ID不能为空')
        if params['vc_username'] is None:
            raise TypeError('账号不能为空')
        if params['l_black_type'] is None:
            raise TypeError('添加类型不能为空')
        if params['vc_token'] is None:
            raise TypeError('令牌不能为空')
        result = getProcedure('UserInfo',
                              (1, params['vc_username'], params['l_uid'],
                               params['l_black_type'], params['vc_token']))
        res = resSuccess(result)
        return HttpResponse(convertJson(res, False))
    except Exception as e:
        # return HttpResponse(convertJsonAscii(resError(str(e)), False))
        return HttpResponse(convertJson(resError(str(e)), False))


def blackList(request):
    '''
    删除黑名单、获取黑名单
    '''
    try:
        params = json.loads(request.body)
        if params['l_uid'] is None:
            raise TypeError('用户ID不能为空')
        result = getProcedure('UserInfo',
                              (params['l_type'], None, params['l_uid'], None, None))
        res = resSuccess(result)
        return HttpResponse(convertJson(res, False))
    except Exception as e:
        # return HttpResponse(convertJsonAscii(resError(str(e)), False))
        return HttpResponse(convertJson(resError(str(e)), False))
