from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


# 用户信息
class UserProfile(AbstractUser):
    # 性别选项
    GENDER_CHOICES = (
        ('male', u'男'),
        ('female', u'女'),
    )
    # 昵称
    nick_name = models.CharField(max_length=20, verbose_name=u'昵称', default="")
    # 生日，可以不填
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(
        max_length=6,
        verbose_name=u'性别',
        choices=GENDER_CHOICES,
        default='female'
    )
    # 地址
    address = models.CharField(max_length=100, verbose_name=u'地址', default='')
    # 电话
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='电话')
    # 头像
    image = models.ImageField(
        upload_to="image/%Y/%m",
        default=u'image/default.png',
        max_length=100
    )

    # meta信息, 后台栏目名称
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


# 邮箱验证码，
class EmailVerifyRecord(models.Model):
    SEND_CHOICES = (
        ('register', u'注册'),
        ('forget', u'找回密码'),
        ("update_email", u"修改邮箱"),
    )
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    # 默认不可为空
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(choices=SEND_CHOICES, max_length=20, verbose_name='发送类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


# 轮播图model
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    image = models.ImageField(
        upload_to='banner/%Y/%m',
        verbose_name=u'轮播图',
        max_length=100
    )
    url = models.URLField(max_length=200, verbose_name=u'访问地址')
    # 默认index很大很靠后，想要靠前要修改index的值
    index = models.IntegerField(default=100, verbose_name=u'顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}轮播'.format(self.title)


