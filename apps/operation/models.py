#from datetime import datetime
from django.db import models
from django.utils import timezone as datetime
# Create your models here.
from users.models import UserProfile
from courses.models import Course


# 用户我要学习的表单
class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'姓名')
    mobile = models.CharField(max_length=11, verbose_name=u'手机')
    course_name = models.CharField(max_length=50, verbose_name=u'课程名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户咨询"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}用户{1},{2}课程'.format(self.name, self.mobile, self.course_name)


# 用户对于课程评论
class CourseComments(models.Model):
    # 课程外键
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u"课程")
    # 用户外键
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户")
    comments = models.CharField(max_length=250, verbose_name=u"评论")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"评论时间")

    class Meta:
        verbose_name = u"课程评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}课程{1}用户评论'.format(self.course, self.user)


# 用户对于课程,机构，讲师的收藏
class UserFavorite(models.Model):
    TYPE_CHOICES = (
        (1, u"课程"),
        (2, u"课程机构"),
        (3, u"讲师")
    )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户")
    # 直接保存收藏类型的id.
    fav_id = models.IntegerField(default=0)
    # 表明收藏的是哪种类型。
    fav_type = models.IntegerField(
        choices=TYPE_CHOICES,
        default=1,
        verbose_name=u"收藏类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"评论时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}的收藏".format(self.user)


# 用户消息表
class UserMessage(models.Model):
        # 因为我们的消息有两种:发给全员和发给某一个用户。
        # 所以如果使用外键，每个消息会对应要有用户。很难实现全员消息。
        # 机智版 为0发给所有用户，不为0就是发给用户的id
    user = models.IntegerField(default=0, verbose_name=u"接收用户")
    message = models.CharField(max_length=500, verbose_name=u"消息内容")

    # 是否已读: 布尔类型 BooleanField False未读,True表示已读
    has_read = models.BooleanField(default=False, verbose_name=u"是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}的消息'.format(self.user)


# 用户课程表
class UserCourse(models.Model):
    # 课程信息
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u"课程")
    # 用户信息
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}的课程{1}'.format(self.user, self.course)
