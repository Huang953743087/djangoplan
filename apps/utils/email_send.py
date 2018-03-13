#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from random import Random

from django.template import loader

__author__ = 'huang'
__time__ = '2018/3/12 18:49'

from users.models import EmailVerifyRecord
# 导入django自带邮件发送模块
from django.core.mail import send_mail, EmailMessage
# 导入设置的邮件信息
from djangoplan.settings import EMAIL_FROM


# 生成随机字符串
def random_str(random_length=8):
    str = ''
    # 生成字符串的可选字符串
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0, length)]
    return str


# 发送注册邮件
def send_register_email(email, send_type="register"):
    # 发送之前先保存到数据库，到时候查询链接是否存在

    # 实例化一个EmailVerifyRecord对象
    email_record = EmailVerifyRecord()
    # 生成随机的code放入链接
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type

    email_record.save()

    # 定义邮件内容:
    # email_title = ""
    # email_body = ""

    if send_type == "register":
        email_title = "huang的练习 注册激活链接"
        email_body = "请点击下面的链接激活你的账号: http://127.0.0.1:9999/active/{0}".format(code)

        # 使用Django内置函数完成邮件发送。四个参数：主题，邮件内容，从哪里发，接受者list
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        # 如果发送成功
        if send_status:
            return True
    elif send_type == 'forget':
        email_title = "找回密码的链接"
        email_body = loader.render_to_string(
            "email_forget.html",  # 需要渲染的html模板
            {
                "active_code": code  # 参数
            }
        )

        # 使用Django内置函数完成邮件发送。四个参数：主题，邮件内容，从哪里发，接受者list
        msg = EmailMessage(email_title, email_body, EMAIL_FROM, [email])
        msg.content_subtype = "html"
        send_status = msg.send()
        # 如果发送成功
        if send_status:
            return True

