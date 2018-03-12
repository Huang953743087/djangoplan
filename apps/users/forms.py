#!/usr/bin/env python3
#-*- coding: utf-8 -*-
__author__ = 'huang'
__time__ = '2018/3/12 11:46'

from django import forms
from captcha.fields import CaptchaField


# 登录表单验证
class LoginForm(forms.Form):
    # 用户名或者密码不能为空
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)

# 注册时验证码
class RegisterForm(forms.Form):
    # 此处email与前端name需要保持一致
    email = forms.EmailField(required=True)
    # 密码不能小于5位
    password = forms.CharField(required=True, min_length=5)
    # 应用验证码
    captcha = CaptchaField()


class ActiveForm(forms.Form):
    # 仅仅是一个验证码
    captcha = CaptchaField()


class ForgetPWDForm(forms.Form):
    # 仅仅是一个验证码
    # 此处email与前端name需保持一致
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


# 重置密码验证
class ModifyPwdForm(forms.Form):
    # 密码不能小于5位
    password1 = forms.CharField(required=True, min_length=5)
    # 密码不能小于5位
    password2 = forms.CharField(required=True, min_length=5)