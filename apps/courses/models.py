from django.db import models
from datetime import datetime
# Create your models here.


# 课程信息
class Course(models.Model):
    # 课程等级
    DEGREE_CHOICES = (
        ('cj', u'初级'),
        ('zj', u'中级'),
        ('gj', u'高级'),
    )
    name = models.CharField(max_length=50, verbose_name=u'课程名')
    desc = models.CharField(max_length=300, verbose_name=u'课程描述')
    # textfield可以不输入长度，输入可以无限长,教程说之后改为富文本
    detail = models.TextField(verbose_name=u'课程详情')
    degree = models.CharField(choices=DEGREE_CHOICES, max_length=2)
    # 使用分钟数做后台记录，前台转换
    learn_times = models.IntegerField(default=0, verbose_name=u'学习时长（分钟）')
    # 点击开始学习就计算人数
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    image = models.ImageField(
        upload_to='courses/%Y/%m',
        verbose_name=u'封面图',
        max_length=100
    )
    # 保存点击量，点一下就算
    cilck_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name


# 章节信息
class Lesson(models.Model):
    # 因为一个课程对应许多章节，所以章节表中课程为外键
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u'课程')
    name = models.CharField(max_length=100, verbose_name=u'章节名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    # 后台显示名称

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name


# 视频信息
class Video(models.Model):
    # 一个章节对应多个视频，所以章节为视频的外键
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=u'章节')
    name = models.CharField(max_length=100, verbose_name=u'视频名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name


# 课程资源
class CourseResource(models.Model):
    # 因为一个课程对应很多资源，所以课程设置为外键
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u'课程')
    name = models.CharField(max_length=100, verbose_name=u'名称')
    # 定义成文件类型，后台会有上次按钮
    # FileField 要求最大长度
    download = models.FileField(
        upload_to='course/resourse/%Y/%m',
        verbose_name=u'资源文件',
        max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程资源'
        verbose_name_plural = verbose_name
