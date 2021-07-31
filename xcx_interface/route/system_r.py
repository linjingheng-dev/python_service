from django.urls import path
from xcx_interface.controller.system.system_msg import getUserInfo, addUserToBlackList, blackList, getInterfaceList

urlpatterns = [
    # 获取接口权限表
    path('getInterfaceList', getInterfaceList, name='getInterfaceList'),
    # 获取用户信息
    path('getUserInfo', getUserInfo, name='getUserInfo'),
    # 将用户添加到黑名单中
    path('addUserToBlackList', addUserToBlackList, name='addUserToBlackList'),
    # 删除黑名单
    path('blackList', blackList, name='blackList')
]
