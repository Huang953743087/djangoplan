#!/usr/bin/env python3
#-*- coding: utf-8 -*-
__author__ = 'huang'
__time__ = '2018/3/10 15:54'

import xadmin
from .models import CourseOrg, CityDict, Teacher


# 城市信息管理
class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


# 机构信息管理
class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'address', 'click_nums', 'fav_nums', 'city', 'add_time']
    search_fields = ['name', 'desc', 'address', 'click_nums', 'fav_nums', 'city']
    list_filter = ['name', 'desc', 'address', 'city', 'click_nums', 'fav_nums', 'add_time']


# 教师信息管理
class TeacherAdmin(object):
    list_display = ['org', 'name', 'points', 'click_nums', 'fav_nums', 'add_time']
    search_fields = ['org', 'name', 'points', 'click_nums', 'fav_nums']
    list_filter = ['org', 'name', 'points', 'click_nums', 'fav_nums', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)