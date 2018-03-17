from datetime import datetime
from django.db import models

# Create your models here.


# 城市信息
class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'城市')
    # 城市描述，备用，不一定展示
    desc = models.CharField(max_length=200, verbose_name=u'描述')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 机构信息
class CourseOrg(models.Model):
    ORG_CHOICES = (
        ("pxjg", u"培训机构"),
        ("gx", u"高校"),
        ("gr", u"个人"),
    )
    name = models.CharField(max_length=50, verbose_name=u'机构名称')
    # 机构描述，后面替换为富文本展示
    desc = models.TextField(verbose_name=u'机构描述')

    click_nums = models.IntegerField(default=0, verbose_name=u'点击量')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏量')
    image = models.ImageField(
        upload_to='org/%Y/%m',
        verbose_name=u'封面图',
        max_length=100)
    address = models.CharField(max_length=150, verbose_name=u'机构地址')
    # 一个城市可以有很多课程机构，通过将city设置外键，变成课程机构的一个字段
    # 可以让我们通过机构找到城市
    city = models.ForeignKey(CityDict, on_delete=models.CASCADE, verbose_name=u'所在城市')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    category = models.CharField(max_length=20, choices=ORG_CHOICES, verbose_name=u"机构类别", default="pxjg")

    class Meta:
        verbose_name = u'课程机构'
        verbose_name_plural = verbose_name

    # 获得教师数量
    def get_teacher_nums(self):
        return self.teacher_set.all().count()

    def get_course_nums(self):
        # 获取章节数
        return self.course_set.all().count()

    def __str__(self):
        return self.name


# 讲师
class Teacher(models.Model):
    # 一个机构可以有很多老师，所以 我们在讲师表把课程机构作为外键，以便通过讲师查找对应的课程机构
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name=u'所属机构')
    name = models.CharField(max_length=50, verbose_name=u"教师名称")
    work_years = models.IntegerField(default=0, verbose_name=u"工作年限")
    work_company = models.CharField(max_length=50, verbose_name=u"就职公司")
    work_position = models.CharField(max_length=50, verbose_name=u"公司职位")
    points = models.CharField(max_length=50, verbose_name=u"教学特点")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    image = models.ImageField(
        default='',
        upload_to="teacher/%Y/%m",
        verbose_name=u"头像",
        max_length=100)
    you_need_know = models.CharField(max_length=300, default=u"好好学习天天向上", verbose_name=u"课程须知")
    teacher_tell = models.CharField(max_length=300, default=u"按时交作业,不然叫家长", verbose_name=u"老师告诉你")
    age = models.IntegerField(default=18, verbose_name=u"年龄")

    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name

    # 获取讲师课程数
    def get_course_nums(self):
        return self.course_set.all().count()

    def __str__(self):
        return '{0}机构的{1}老师'.format(self.org, self.name)


