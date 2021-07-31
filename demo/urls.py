from django.urls import path
from . import views

# 请求路由
urlpatterns = [
    # ex: /demo/
    path('', views.index, name='index'),
    # ex: /demo/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /demo/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /demo/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
