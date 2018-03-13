"""djangoplan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.static import serve

import xadmin
from organization.views import OrgView
from settings import MEDIA_ROOT
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPWDView, ResetView, ModifyPwdView

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # TemplateView.as_view会将template转换为view
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    # 注册登录等用户相关 ↓↓↓↓ #
    # 登录界面
    path('login/',  LoginView.as_view(), name='login'),
    # 注册界面
    path('register/', RegisterView.as_view(), name='register'),
    # 验证码
    path("captcha/", include('captcha.urls')),
    # 验证激活是否成功
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name="user_active"),
    # 忘记密码验证
    path('forget_pwd/', ForgetPWDView.as_view(), name='forget_pwd'),
    # 重设密码
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name="reset_pwd"),
    # 重设成功
    path('modify_pwd/', ModifyPwdView.as_view(), name="modify_pwd"),
    # 注册登录等用户相关 ↑↑↑↑ #
    # 机构显示
    path('org_list/', OrgView.as_view(), name='org_list'),
    # 图片处理
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT })
]
