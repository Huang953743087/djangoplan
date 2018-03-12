#!/usr/bin/env python3
#-*- coding: utf-8 -*-

__author__ = 'huang'
__time__ = '2018/3/10 11:07'
from django.contrib.auth.models import Permission, Group

from courses.models import Course, Lesson, Video, CourseResource
from operation.models import UserAsk, UserMessage, UserFavorite, UserCourse, CourseComments
from organization.models import CityDict, Teacher, CourseOrg
from xadmin.models import Log


import xadmin

from .models import EmailVerifyRecord, UserProfile, Banner
from xadmin import views


# 定义email管理
class EmailVerifyRecordAdmin(object):
    # 添加显示列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 添加搜索
    search_fields = ['code', 'email', 'send_type', ]
    # 添加筛选字段
    list_filter = ['code', 'email', 'send_type', 'send_time']


# 定义轮播图管理程序
class BannerAdmin(object):
    # 添加显示列
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    # 添加搜索
    search_fields = ['title', 'image', 'url', 'index']
    # 添加筛选字段
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '黄泽昊的学习后台'
    site_footer = 'Huang`s study'
    # 收起菜单
    menu_style = 'accordion'

    def get_site_menu(self):
        return (
            {'title': '课程管理', 'menus': (
                {'title': '课程信息', 'url': self.get_model_url(Course, 'changelist')},
                {'title': '章节信息', 'url': self.get_model_url(Lesson, 'changelist')},
                {'title': '视频信息', 'url': self.get_model_url(Video, 'changelist')},
                {'title': '课程资源', 'url': self.get_model_url(CourseResource, 'changelist')},
                {'title': '课程评论', 'url': self.get_model_url(CourseComments, 'changelist')},
            )},
            {'title': '机构管理', 'menus': (
                {'title': '所在城市', 'url': self.get_model_url(CityDict, 'changelist')},
                {'title': '机构讲师', 'url': self.get_model_url(Teacher, 'changelist')},
                {'title': '机构信息', 'url': self.get_model_url(CourseOrg, 'changelist')},
            )},
            {'title': '用户管理', 'menus': (
                {'title': '用户信息', 'url': self.get_model_url(UserProfile, 'changelist')},
                {'title': '用户验证', 'url': self.get_model_url(EmailVerifyRecord, 'changelist')},
                {'title': '用户课程', 'url': self.get_model_url(UserCourse, 'changelist')},
                {'title': '用户收藏', 'url': self.get_model_url(UserFavorite, 'changelist')},
                {'title': '用户消息', 'url': self.get_model_url(UserMessage, 'changelist')},
            )},

            {'title': '系统管理', 'menus': (
                {'title': '用户咨询', 'url': self.get_model_url(UserAsk, 'changelist')},
                {'title': '首页轮播', 'url': self.get_model_url(Banner, 'changelist')},
                {'title': '用户分组', 'url': self.get_model_url(Group, 'changelist')},
                {'title': '用户权限', 'url': self.get_model_url(Permission, 'changelist')},
                {'title': '日志记录', 'url': self.get_model_url(Log, 'changelist')},
            )},)


# 注册
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)