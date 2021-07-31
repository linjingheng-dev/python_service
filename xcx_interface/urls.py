from django.urls import include, path

urlpatterns = [
    # 系统逻辑
    path('system/', include('xcx_interface.route.system_r')),
    # 菜单业务
    path('menu/', include('xcx_interface.route.menu_r'))
]
