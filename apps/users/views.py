from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.shortcuts import render

from django.views.generic.base import View

from users.forms import LoginForm, RegisterForm, ActiveForm, ForgetPWDForm, ModifyPwdForm
from users.models import UserProfile,EmailVerifyRecord


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
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误'})

        else:
            return render(request, 'login.html', {'login_form' : login_form})


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
                return render(request, 'index.html')
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
            return render(request, "password_reset.html", {"email": email, "modiypwd_form":modiypwd_form})