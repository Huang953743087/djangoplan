from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import  render_to_response
from django.views.generic.base import View

from courses.models import Course
from operation.models import UserCourse, UserFavorite, UserMessage
from organization.models import CourseOrg, Teacher
from users.forms import LoginForm, RegisterForm, ActiveForm, ForgetPWDForm, ModifyPwdForm, UploadImageForm, \
    UpdateUserInfoForm
from users.models import UserProfile, EmailVerifyRecord, Banner

# def user_login(request):
#     #前端向后端发送的请求方式：get。post
#     #登陆为post请求
#     if request.method == 'POST':
#         user_name = request.POST.get('username', '')
#         pass_word = request.POST.get('password', '')
#         #成功返回user对象，失败返回null
#         user = authenticate(username=user_name, password=pass_word)
#
#         #如果不是null说明验证成功
#         if user is not None:
#             # login_in 两参数：request, user
#             # 实际是对request写了一部分东西进去，然后在render的时候：
#             # request是要render回去的。这些信息也就随着返回浏览器。完成登录
#             login(request, user)
#             # 跳转到首页，user ，request会被带到首页
#             return render(request, 'index.html')
#         #没有说明里面值是None,再次跳转到主页面
#         else:
#             return render(request, 'login.html', {"msg":"用户名或密码错误"})
#
#
#     elif request.method == 'GET':
#         # render渲染html并返回
#         # render三变量:request 模板名称， 一个字典写明传给前端的值
#         return render(request, 'login.html', {})

# 继承view类更加方便。
from utils.email_send import send_register_email


# 注册页面
class RegisterView(View):
    def get(self, request):
        # get方法直接返回页面
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        # is_valid 判断如果不符合Form中的条件会返回NONE
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            pass_word = request.POST.get('password', '')
            # 实例化userprofile
            # 保存用户名
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_message = UserMessage()
            user_message.user = user_profile.id
            user_message.message = "欢迎注册huang的练习!!"
            user_message.save()

            # 加密保存
            user_profile.password = make_password(pass_word)
            # 新用户默认处于未激活状态
            user_profile.is_active = False
            user_profile.save()
            if send_register_email(user_name, 'register'):
                return render(request, 'register.html', {})


# 登陆页面
class LoginView(View):
    # 可以直接调用方法而不用判断
    def get(self, request):
        # render函数直接返回
        # request , 模板， {传给前端的值}
        return render(request, 'login.html', {})

    def post(self, request):
        # 类实例化需要一个字典参数dict:request.POST就是一个QueryDict所以直接传入
        # POST中的username与password，会对应到form中
        login_form = LoginForm(request.POST)
        # is_valid判断我们的字段是否对应原有逻辑，验证失败直接跳回login页面
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')

            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                # login_in 两参数：request, user
                # 实际是对request写了一部分东西进去，然后在render的时候：
                # request是要render回去的。这些信息也就随着返回浏览器。完成登录
                login(request, user)
                # 跳转到首页 user request会被带回到首页
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误'})

        else:
            return render(request, 'login.html', {'login_form' : login_form})


# 退出登录
class LogoutView(View):
    def get(self, request):
        # django 自带退出方法
        logout(request)
        return HttpResponseRedirect(reverse("index"))


# 登陆可使用用户名或邮箱验证
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # 不希望用户存在两个，get只能有一个。两个是get失败的一种原因 Q为使用并集查询

            user = UserProfile.objects.get(Q(username=username) | Q(email=username))

            # django的后台中密码加密：所以不能password==password
            # UserProfile继承的AbstractUser中有def check_password(self, raw_password):

            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 用户激活验证
class ActiveUserView(View):
    def get(self, request, active_code):
        # 判断激活链接是否存在
        all_record = EmailVerifyRecord.objects.filter(code=active_code)
        register_form = RegisterForm(request.GET)
        if all_record:
            for record in all_record:
                # 获取到邮箱
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()

                return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'register.html', {'msg': "您的激活链接无效", 'register_form': register_form})


# 忘记密码页面
class ForgetPWDView(View):
    def get(self, request):
        forget_form = ForgetPWDForm()
        return render(request, 'forgetpwd.html', {'forget_form': forget_form})

    def post(self, request):
        forget_form = ForgetPWDForm(request.POST)
        # form验证合法情况下取出email
        if forget_form.is_valid():
            email = request.POST.get("email", "")
            # 发送找回密码邮件
            send_register_email(email, "forget")
            # 发送完毕返回登录页面并显示发送邮件成功。
            return render(request, "login.html", {"msg": "重置密码邮件已发送,请注意查收"})
            # 如果表单验证失败也就是他验证码输错等。
        else:
            return render(request, "forgetpwd.html", {"forget_form": forget_form})


# 重设密码
class ResetView(View):
    def get(self, request, active_code):
        # 查询邮箱验证记录是否存在
        all_record = EmailVerifyRecord.objects.filter(code=active_code)
        # 如果不为空也就是有用户
        active_form = ActiveForm(request.GET)
        if all_record:
            for record in all_record:
                # 获取到对应的邮箱
                email = record.email
                # 将email传回来
                return render(request, "password_reset.html", {"email": email})
        # 自己瞎输的验证码
        else:
            return render(
                request, "forgetpwd.html", {
                    "msg": "您的重置密码链接无效,请重新请求", "active_form": active_form})


# 改变密码的view
class ModifyPwdView(View):
    def post(self, request):
        modiypwd_form = ModifyPwdForm(request.POST)
        if modiypwd_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            email = request.POST.get("email", "")
            # 如果两次密码不相等，返回错误信息
            if pwd1 != pwd2:
                return render(request, "password_reset.html", {"email": email, "msg": "密码不一致"})
            # 如果密码一致
            user = UserProfile.objects.get(email=email)
            # 加密成密文
            user.password = make_password(pwd2)
            # save保存到数据库
            user.save()
            return render(request, "login.html", {"msg": "密码修改成功，请登录"})
        # 验证失败说明密码位数不够。
        else:
            email = request.POST.get("email", "")
            return render(request, "password_reset.html", {"email": email, "modiypwd_form": modiypwd_form})


class UserInfoView(LoginRequiredMixin, View):
    """
    进入用户个人信息
    """
    # 未登录访问此视图会自动跳转到登录界面
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request):
        return render(request, 'usercenter-info.html', {})

    def post(self, request):
        user_info_form = UpdateUserInfoForm(request.POST, instance=request.user)
        if user_info_form.is_valid():
            user_info_form.save()
            return HttpResponse('{"status": "success"}', content_type='application/json')


class UpdateImageView(LoginRequiredMixin, View):
    """
    修改用户头像
    """
    login_url = '/login/'
    redirect_field_name = 'next'

    def post(self, request):
        image_form = UploadImageForm(request.POST, request.FILES, )
        if image_form.is_valid():
            # form 中保存就能直接更改user头像
            image_form.save()
            # 另一种方法
            # # 取出cleaned data中的值,一个dict
            # image = image_form.cleaned_data['image']
            # request.user.image = image
            # request.user.save()
            return HttpResponse('{"status":"success",}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail", }', content_type='application/json')


class UpdatePWDView(LoginRequiredMixin, View):
    """
    修改密码
    """
    login_url = '/login/'
    redirect_field_name = 'next'

    def post(self, request):
        modifpwd_form = ModifyPwdForm(request.POST)
        if modifpwd_form.is_valid():
            # 验证密码是否一致
            password1 = request.POST.get('password1', '')
            password2 = request.POST.get('password2', '')
            if password1 != password2:
                return HttpResponse('{"status":"fail", "msg":"密码不一致",}', content_type='application/json')
            user = request.user
            user.password = make_password(password2)
            user.save()
            return HttpResponse('{"status":"success",}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"密码输入有误"}', content_type='application/json')


class SendEmailView(LoginRequiredMixin, View):
    """
    发送更新用户邮箱的验证码
    """
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request):
        email = request.GET.get('email', '')
        if UserProfile.objects.filter(email=email):
            return HttpResponse('{"status": "fail", "msg": "邮箱已存在"}', content_type='application/json')
        if send_register_email(email, "update_email"):
            return HttpResponse('{"status": "success"}', content_type='application/json')
        else:
            return  HttpResponse('{"status": "fail", "msg":"发送出错, 请联系管理员"}', content_type='application/json')


class UpdateEmailView(LoginRequiredMixin, View):
    """
    更新用户邮箱
    """
    login_url = '/login/'
    redirect_field_name = 'next'

    def post(self, request, active_code):
        email = request.POST.get('email', '')
        code = request.POST.get('code', '')

        existed_records = EmailVerifyRecord.objects.filter(email=email, code=active_code, send_type='update_email')
        if existed_records:
            user = request.user
            user.email = email
            user.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"email": "验证码错误"}', content_type='application/json')


class UserCourseView(LoginRequiredMixin, View):
    """
    用户课程中心
    """
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request):
        user_courses = UserCourse.objects.filter(user=request.user)
        courses = []
        for course in user_courses:
            course_id = course.course
            courses.append(course_id)
        return render(request, 'usercenter-mycourse.html',
                      {
                          'user_courses': courses,

        })


class FavOrgView(LoginRequiredMixin, View):
    """
    用户收藏机构列表
    """
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request):
        org_list = []
        fav_orgs = UserFavorite.objects.filter(user=request.user, fav_type=2)
        # fav_orgs存放了id，需要通过id找到机构对象
        for fav_org in fav_orgs:
            # 取出fav_id
            org_id = fav_org.fav_id
            # 获取这个机构对象
            org = CourseOrg.objects.get(id=org_id)
            org_list.append(org)
        return render(request, 'usercenter-fav-org.html', {
                'org_list': org_list
            })


class FavTeacherView(LoginRequiredMixin, View):
    """
    用户收藏教师列表
    """
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request):
        teacher_list = []
        fav_teachers = UserFavorite.objects.filter(user=request.user, fav_type=3)
    # fav_orgs存放了id，需要通过id找到机构对象
        for fav_teacher in fav_teachers:
            # 取出fav_id
            teacher_id = fav_teacher.fav_id
            # 获取这个机构对象
            teacher = Teacher.objects.get(id=teacher_id)
            teacher_list.append(teacher)
        return render(request, 'usercenter-fav-teacher.html', {
                'teacher_list': teacher_list
            })


class FavCourseView(LoginRequiredMixin, View):
    """
    用户收藏课程列表
    """
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request):
        course_list = []
        fav_courses = UserFavorite.objects.filter(user=request.user, fav_type=1)
    # fav_courses存放了id，需要通过id找到课程对象
        for fav_course in fav_courses:
            # 取出fav_id
            course_id = fav_course.fav_id
            # 获取这个机构对象
            course = Course.objects.get(id=course_id)
            course_list.append(course)
        return render(request, 'usercenter-fav-course.html', {
                'course_list': course_list
            })


class MyMessageView(LoginRequiredMixin, View):
    """
    用户消息
    """
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request):
        all_message = UserMessage.objects.filter(user=request.user.id)
        all_unread_messages = UserMessage.objects.filter(user=request.user.id, has_read=False)
        for unread_message in all_unread_messages:
            unread_message.has_read = True
            unread_message.save()
        # 尝试获取前台get请求传递过来的page参数
        # 如果是不合法的配置参数默认返回第一页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # 这里指从allorg中取五个出来，每页显示4个
        p = Paginator(all_message, 4)
        messages = p.page(page)
        return render(request, "usercenter-message.html", {
            "messages": messages,
        })


class IndexView(View):
    def get(self, request):
        # 轮播图
        all_banner = Banner.objects.all().order_by('index')[:5]
        # 非轮播课程
        courses = Course.objects.filter(is_banner=False)[:6]
        # 轮播课程
        banner_course = Course.objects.filter(is_banner=True)[:3]
        # 机构列表
        org_list = CourseOrg.objects.all().order_by('-click_nums')[:15]
        return render(request, 'index.html',
                      {
                          'all_banners': all_banner,
                          'all_courses': courses,
                          'banner_courses': banner_course,
                          'all_org': org_list,
                      })


# 404对应处理view
def page_not_found(request):

    response = render_to_response("404.html", {

    })
    # 设置response的状态码
    response.status_code = 404
    return response


def page_is_403(request):
    response = render_to_response("403.html", {
    })
    # 设置response的状态码
    response.status_code = 403
    return response


def page_is_500(request):
    response = render_to_response("500.html", {
    })
    # 设置response的状态码
    response.status_code = 500
    return response