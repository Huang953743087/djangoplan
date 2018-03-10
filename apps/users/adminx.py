#!/usr/bin/env python3
#-*- coding: utf-8 -*-
__author__ = 'huang'
__time__ = '2018/3/10 11:07'

import xadmin

from .models import EmailVerfyRecord
from .models import Banner


# 定义email管理
class EmailVerfyRecordAdmin(object):
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


# 注册
xadmin.site.register(EmailVerfyRecord, EmailVerfyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)