"""
@Author 林景恒
@Date 20200719
@LastModifyDate --
@Desc 获取菜品信息，如列表、详情
"""
from django.http import HttpResponse
from xcx_interface.utils.util import convertJson
from xcx_interface.utils.util import executeSelect, resSuccess, resError, convertJsonAscii


# 获取菜品列表信息
def getMenuList(request):
    try:
        getType = request.GET.get('type')
        type = getType if getType is not None else 'FOOD_CATEGORY'
        sql = "select * from t_menu a inner join t_dictionaries b on a.vc_category=b.vc_key and b.vc_type='%s' order by b.vc_key ASC" % (type)
        row = executeSelect(sql, False)
        res = resSuccess(row)
        return HttpResponse(convertJson(res, False))
    except Exception as e:
        return HttpResponse(convertJsonAscii(resError(str(e)), False))


# 获取菜品详情
def getMenuDetailMsg(request):
    return HttpResponse("获取菜品详情")
