#!/usr/bin/env python3
#-*- coding: utf-8 -*-
__author__ = 'huang'
__time__ = '2018/3/10 11:07'

import xadmin

from .models import EmailVerfyRecord


# 定义email管理
class EmailVerfyRecordAdmin(object):
    # 添加显示列
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type', ]
    list_filter = ['code', 'email', 'send_type', 'send_time']


# 注册
xadmin.site.register(EmailVerfyRecord, EmailVerfyRecordAdmin)