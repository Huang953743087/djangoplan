from django.db import models
from datetime import datetime
# Create your models here.


# 课程信息
from organization.models import CourseOrg, Teacher


class Course(models.Model):
    # 课程等级
    DEGREE_CHOICES = (
        ('cj', u'初级'),
        ('zj', u'中级'),
        ('gj', u'高级'),
    )
    teacher = models.ForeignKey(Teacher, verbose_name=u"讲师", null=True, blank=True)
    course_org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name=u"所属机构", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u'课程名')
    desc = models.CharField(max_length=300, verbose_name=u'课程描述')
    # textfield可以不输入长度，输入可以无限长,教程说之后改为富文本
    detail = models.TextField(verbose_name=u'课程详情')
    # 课程等级
    degree = models.CharField(choices=DEGREE_CHOICES, max_length=2)
    # 使用分钟数做后台记录，前台转换
    learn_times = models.IntegerField(default=0, verbose_name=u'学习时长（分钟）')
    # 点击开始学习就计算人数
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    tag = models.CharField(max_length=15, verbose_name=u"课程标签", default=u"")
    image = models.ImageField(
        upload_to='courses/%Y/%m',
        verbose_name=u'封面图',
        max_length=100
    )
    # 保存点击量，点一下就算
    cilck_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    category = models.CharField(max_length=20, default=u"", verbose_name=u"课程类别")

    def get_zj_nums(self):
        # 获取章节数
        return self.lesson_set.all().count()

    def get_learn_users(self):
        # 谁的里面添加了它做外键，他都可以取出来
        # 获取学习的人
        return self.usercourse_set.all()[:5]

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '《{0}》'.format(self.name)


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

    def __str__(self):
        return '《{0}》课程的《{1}》章节'.format(self.course, self.name)


# 视频信息
class Video(models.Model):
    # 一个章节对应多个视频，所以章节为视频的外键
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=u'章节')
    name = models.CharField(max_length=100, verbose_name=u'视频名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    url = models.CharField(max_length=200, default="http://www.ihave20sp.xyz/", verbose_name=u"访问地址")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}章，{1}'.format(self.lesson, self.name)


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

    def __str__(self):
        return '《{0}》课程的{1}文件'.format(self.course, self.name)
