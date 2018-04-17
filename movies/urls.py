"""为应用程序movies定义URL模式"""
from django.conf.urls import url
from django.urls import re_path
from django.contrib.auth.views import login


from . import views

app_name = '[movies]'
urlpatterns = [
    url(r'^videos/$', views.video , name="video"),
]
