#!/usr/bin/env python3
#-*- coding: utf-8 -*-
__author__ = 'huang'
__time__ = '2018/3/14 16:20'
from organization.views import OrgListView, OrgHomeView, OrgCourseView, OrgTeacherView, OrgDescView, AddFavView, \
    TeacherListView, TeacherDescView

from django.urls import path, re_path

app_name = 'organization'
urlpatterns = [
    # 课程机构列表
    path('list/', OrgListView.as_view(), name='org_list'),
    # 机构首页
    re_path('home/(?P<org_id>\d+)/', OrgHomeView.as_view(), name="org_home"),
    # 访问课程
    re_path('course/(?P<org_id>\d+)/', OrgCourseView.as_view(), name="org_course"),
    # 访问机构描述
    re_path('desc/(?P<org_id>\d+)/', OrgDescView.as_view(), name="org_desc"),
    # 访问机构讲师
    re_path('teacher/(?P<org_id>\d+)/', OrgTeacherView.as_view(), name="org_teacher"),
    # 添加收藏
    path('add_fav/', AddFavView.as_view(), name="add_fav"),
    # 访问讲师列表
    path('teacher_list/', TeacherListView.as_view(), name="teacher_list"),
    # 教师详情
    re_path('teacher/detail/(?P<teacher_id>\d+)/', TeacherDescView.as_view(), name="teacher_detail"),
   ]