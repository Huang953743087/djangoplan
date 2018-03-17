#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from users.views import UserInfoView, UpdateImageView, UpdatePWDView, SendEmailView, UpdateEmailView, UserCourseView
from users.views import FavCourseView, FavOrgView, FavTeacherView
__author__ = 'huang'
__time__ = '2018/3/17 16:14'

from django.urls import path, re_path
app_name = 'users'

urlpatterns = [
    # 用户详情
    path('info/', UserInfoView.as_view(), name='user_info'),
    # 更新用户头像
    path('update/image/', UpdateImageView.as_view(), name='update_image'),
    # 更新用户密码
    path('update/password/', UpdatePWDView.as_view(), name='update_pwd'),
    # 发送更改邮箱的验证码
    path('send_email_code/', SendEmailView.as_view(), name='send_email_code'),
    # 重设邮箱
    path('update_email/', UpdateEmailView.as_view(), name="update_email"),
    # 用户课程列表
    path('courses/', UserCourseView.as_view(), name='user_course'),
    # 用户收藏的各类
    path('fav_course/', FavCourseView.as_view(), name='fav_course'),
    path('fav_org/', FavOrgView.as_view(), name='fav_org'),
    path('fav_teacher/', FavTeacherView.as_view(), name='fav_teacher'),
]