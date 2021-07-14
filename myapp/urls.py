# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/7/14 下午7:12

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name="myadd"),
]
