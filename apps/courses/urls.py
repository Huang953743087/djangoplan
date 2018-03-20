#!/usr/bin/env python3
#-*- coding: utf-8 -*-


__author__ = 'huang'
__time__ = '2018/3/15 13:10'

from courses.views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddCommentsView, VideoPlayView
from django.urls import path, re_path

app_name = 'courses'

urlpatterns = [
    # 课程列表
    path('list/', CourseListView.as_view(), name='list'),
    # 课程详情
    re_path('course/(?P<course_id>\d+)/', CourseDetailView.as_view(), name="course_detail"),
    # 课程章节列表
    re_path('info/(?P<course_id>\d+)/', CourseInfoView.as_view(), name='course_info'),
    # 课程评论
    re_path('comments/(?P<course_id>\d+)/', CommentsView.as_view(), name="course_comments"),
    # 添加课程评论
    path('add_comment/', AddCommentsView.as_view(), name="add_comment"),
    # 视频信息
    re_path('video/(?P<course_id>\d+)/', VideoPlayView.as_view(), name="video_play"),
]