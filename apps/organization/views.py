from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from operation.models import UserFavorite
from organization.forms import UserAskForm
from .models import CourseOrg, CityDict, Teacher
from pure_pagination import PageNotAnInteger, EmptyPage, Paginator
from django.http import HttpResponse


class OrgView(View):
    """
    机构列表
    """
    def get(self, request):
        # 获取所有城市
        all_citys = CityDict.objects.all()
        # 获取所有机构
        all_orgs = CourseOrg.objects.all()
        # 统计机构数量
        org_nums = all_orgs.count()
        sort = request.GET.get('sort', "")
        # 排序
        if sort:
            if sort == "students":
                all_orgs = all_orgs.order_by("-students")
            elif sort == "courses":
                all_orgs = all_orgs.order_by("-click_nums")
        # 对课程机构进行分页
        # 尝试获取前台get请求传递过来的page参数
        # 如果是不合法的配置参数默认返回第一页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # 从all——org中每页取5个
        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)

        return render(request, 'org-list.html', {
            'all_citys': all_citys,
            'all_orgs': orgs,
            'org_nums': org_nums,
            'sort': sort,
        })


class AddUserAskView(View):
    """
    用户添加我要学习时的操作
    """
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():

            # 这里是modelform和form的区别
            # 它有model的属性
            # 当commit为true进行真正保存
            user_ask = userask_form.save(commit=True)
            # 如果保存成功,返回json字符串,后面content type是告诉浏览器的,
            return HttpResponse("{'status': 'success'}", content_type='application/json')
        else:
            # 如果保存失败，返回json字符串,并将form的报错信息通过msg传递到前端
            return HttpResponse("{'status':'fail', 'msg':{0}}".format(userask_form.errors), content_type='application/json')


class OrgHomeView(View):
    """
    机构课程首页
    """
    def get(self, request, org_id):
        # 根据id寻找到机构
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 通过课程机构找到课程。内建的变量，找到指向这个字段的外键引用
        all_courses = course_org.course_set.all()[:4]
        all_teachers = course_org.teacher_set.all()[:2]
        has_fav = False
        # 必须是用户已登录我们才需要判断。
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        return render(request, 'org-detail-homepage.html', {
            'all_courses': all_courses,
            'all_teachers': all_teachers,
            'course_org': course_org,
            'has_fav': has_fav,
        })


class OrgCourseView(View):
    """
    机构课程列表
    """
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 通过课程机构找到课程。内建的变量，找到指向这个字段的外键引用
        all_courses = course_org.course_set.all()
        has_fav = False
        # 必须是用户已登录我们才需要判断。
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        return render(request, 'org-detail-course.html', {
            'all_courses': all_courses,
            'course_org': course_org,
            'has_fav': has_fav,
        })


class OrgDescView(View):
    """
   机构描述详情页
    """
    def get(self, request, org_id):
        # 向前端传值，表明现在在home页
        current_page = "desc"
        # 根据id取到课程机构
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 通过课程机构找到课程。内建的变量，找到指向这个字段的外键引用
        # 向前端传值说明用户是否收藏
        has_fav = False
        # 必须是用户已登录我们才需要判断。
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        return render(request, 'org-detail-desc.html', {
            'course_org': course_org,
            "current_page": current_page,
            "has_fav": has_fav,
        })


class OrgTeacherView(View):
    """
   机构讲师列表页
    """
    def get(self, request, org_id):
        # 向前端传值，表明现在在home页
        current_page = "teacher"
        # 根据id取到课程机构
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 通过课程机构找到课程。内建的变量，找到指向这个字段的外键引用
        all_teachers = course_org.teacher_set.all()
        # 向前端传值说明用户是否收藏
        has_fav = False
        # 必须是用户已登录我们才需要判断。
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
                course_org.fav_nums += 1
                course_org.save()
        return render(request, 'org-detail-teachers.html', {
            'all_teachers': all_teachers,
            'course_org': course_org,
            "current_page": current_page,
            "has_fav": has_fav
        })


class TeacherListView(View):
    def get(self, request):
        # 获取所有机构
        all_teachers = Teacher.objects.all()
        # 统计机构数量
        teacher_nums = all_teachers.count()
        sort = request.GET.get('sort', "")
        hot_teacher = all_teachers.order_by("-course_nums")[:3]
        # 排序
        if sort:
            if sort == "hot":
                all_teachers = all_teachers.order_by("-course_nums")
        # 对课程机构进行分页
        # 尝试获取前台get请求传递过来的page参数
        # 如果是不合法的配置参数默认返回第一页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # 从all——org中每页取5个
        p = Paginator(all_teachers, 5, request=request)
        teachers = p.page(page)

        return render(request, 'teachers-list.html', {
            'all_teachers': teachers,
            'teacher_nums': teacher_nums,
            'sort': sort,
            'hot_teacher': hot_teacher,
        })


class TeacherDescView(View):
    """
   教师描述详情页
    """
    def get(self, request, teacher_id):
        # 向前端传值，表明现在在详情页
        current_page = "desc"
        # 根据id取到教师
        hot_teacher = Teacher.objects.all().order_by('-click_nums')[:3]
        teacher = Teacher.objects.get(id=int(teacher_id))
        # 通过课程机构找到课程。内建的变量，找到指向这个字段的外键引用
        hot_course = teacher.course_set.all().order_by('-click_nums')[:3]
        # 向前端传值说明用户是否收藏
        # 必须是用户已登录我们才需要判断。
        has_fav_teacher = False
        if UserFavorite.objects.filter(user=request.user, fav_type=3, fav_id=teacher.id):
            has_fav_teacher = True
            teacher.fav_nums += 1
            teacher.save()
        has_fav_org = False
        if UserFavorite.objects.filter(user=request.user, fav_type=2, fav_id=teacher.org.id):
            has_fav_org = True
            teacher.org.fav_nums += 1
            teacher.org.save()

        return render(request, 'teacher-detail.html', {
            'teacher': teacher,
            "current_page": current_page,
            "has_fav_teacher": has_fav_teacher,
            "has_fav_org": has_fav_org,
            'hot_course': hot_course,
            'hot_teacher': hot_teacher,
        })


class AddFavView(View):
    """
    收藏功能
    """
    def post(self, request):
        # 标明取到的收藏类型的具体id
        # 默认值为0因为不能为空
        id = request.POST.get('fav_id', 0)
        # 取到收藏的类别
        type = request.POST.get('pav_type', 0)

        # 判断收藏还是取消收藏
        # 判断是否登录
        if not request.user.is_authenticated:
            # 未登录返回json未登录， 跳转到登录页面是在ajax中做
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        exist_records = UserFavorite.objects.filter(user=request.user, fav_id=int(id), fav_type=int(type))
        if exist_records:
            exist_records.delete()
            return HttpResponse('{"status":"success", "msg":"取消收藏"}', content_type='application/json')
        else:
            user_fav = UserFavorite()
            # 过滤掉未取到fav_id type的默认情况
            if int(type) > 0 and int(id) > 0:
                user_fav.fav_id = int(id)
                user_fav.fav_type = int(type)
                user_fav.user = request.user
                user_fav.save()
                return HttpResponse('{"status":"success", "msg":"已收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail", "msg":"收藏出错"}', content_type='application/json')
