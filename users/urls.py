"""为应用程序users定义URL模式"""
from django.conf.urls import url
from django.urls import re_path
from django.contrib.auth.views import login


from . import views

app_name = '[users]'
urlpatterns = [
    # 登录页面
    re_path(r'^users/login/$', login ,{'template_name':'users/login.html'},name='login'),
    # 注销页面
    re_path(r'^users/logout/$', views.logout_view,  name= 'logout'),
    # 注册页面
    re_path(r'^users/register/$', views.register, name = 'register'),


]
