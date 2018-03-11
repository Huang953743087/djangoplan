#!/usr/bin/env python3
#-*- coding: utf-8 -*-
__author__ = 'huang'
__time__ = '2018/3/10 16:06'

import xadmin
from .models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse


# 用户咨询管理
class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


# 用户评论管理
class CourseCommentsAdmin(object):
    list_display = ['course', 'user', 'comments', 'add_time']
    search_fields = ['course', 'user', 'comments']
    list_filter = ['course', 'user', 'comments', 'add_time']


# 用户收藏管理
class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


# 用户消息管理
class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


# 用户课程管理
class UserCourseAdmin(object):
    list_display = ['course', 'user', 'add_time']
    search_fields = ['course', 'user']
    list_filter = ['course', 'user', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)