from django.urls import path
from xcx_interface.controller.menu.menu_msg import getMenuList

urlpatterns = [
    # 获取菜单列表
    path('getMenuList', getMenuList, name='getMenuList')
]
