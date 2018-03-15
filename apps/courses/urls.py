#!/usr/bin/env python3
#-*- coding: utf-8 -*-


__author__ = 'huang'
__time__ = '2018/3/15 13:10'

from courses.views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddCommentsView
from django.urls import path, re_path

app_name = 'courses'

urlpatterns = [
    path('list/', CourseListView.as_view(), name='list'),
    re_path('course/(?P<course_id>\d+)/', CourseDetailView.as_view(), name="course_detail"),
    re_path('info/(?P<course_id>\d+)/', CourseInfoView.as_view(), name='course_info'),
    re_path('comments/(?P<course_id>\d+)/', CommentsView.as_view(), name="course_comments"),
    path('add_comment/', AddCommentsView.as_view(), name="add_comment"),
    path('video/(?P<video_id>\d+)/', VideoPlayView.as_view(), name="video_play"),
]