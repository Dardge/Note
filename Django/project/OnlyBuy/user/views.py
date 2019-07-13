from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth import hashers  # 用户密码加密
from django.db import utils
from django.contrib import auth
import json
from django.contrib.auth.decorators import login_required  # 用于登陆状态验证


# Create your views here.


def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    else:
        username = request.POST.get('uname', '')
        password = request.POST.get('upwd')
        password2 = request.POST.get('upwdconfirm', '')
        phone = request.POST.get('uphone', '')
        email = request.POST.get('uemail', '')
        # 做验证判断
        # 验证用户是否注册过
        if User.objects.filter(username=username).first():
            return HttpResponse('该用户已存在')
        # 验证两次密码是否一致
        if password != password2:
            return HttpResponse('两次密码不一致')
        # 判断是否有未填写信息
        if not (username and password and phone and email):
            return HttpResponse('输入内容不能为空')

        # 注册用户业务
        # 密码加密
        password_sha1 = hashers.make_password(password, None, 'pbkdf2_sha1')
        try:
            User.objects.create(username=username, nickname=username, password=password_sha1, phone=phone, email=email)
        except utils.DatabaseError as e:
            return HttpResponse('<h1>注册失败<h1>' + "<h1>%s</h1>" % e)
        return HttpResponse('<h1>注册成功<h1>' + "<h1><a href='/'>返回user首页</a></h1>")


def login(request):
    # 判断是否已登录过
    # 如果已登录 返回首页
    if request.user.is_authenticated():
        return redirect('/')
    if request.method == 'GET':
        # login_requested装饰器强制跳转会发送一个键为next的GET请求
        # /user/login/?next=/user/logout/
        # 确定查询字符串中是否有next值，如果有值登陆之后跳转到该值的页面，交给POST使用
        next1 = request.GET.get('next', '/')
        # 先获取到值  将值放入表单中随表单提交
        # 放到hidden隐藏域中
        return render(request, 'user/login.html', locals())
    else:
        if request.session.get('verifycode').lower() != request.POST.get('ma').lower():
            return HttpResponse('验证码错误')
        data = request.POST
        if not (data['username'] and data['password']):
            return HttpResponse('用户名和密码不能为空')
        user = User.objects.filter(username=data['username']).first()
        if not user:  # 如果此用户不存在
            return HttpResponse('用户不存在')
        user = auth.authenticate(request=request, username=data['username'], password=data['password'])
        if user and user.is_active:  # 如果密码正确
            # 通过login将user和request对象关联，此后可以通过request.user的方式访问用户
            auth.login(request, user)
            resp = HttpResponse('登陆成功')
            request.session['mysession'] = user.username  # 保存session
            if request.POST.get('isActive'):
                if 'user' in request.COOKIES:  # 如果cookie里存在存放数据的user,则获取cookie并判断是否需要添加数据
                    user_list = request.COOKIES['user']
                    user_list = json.loads(user_list)
                    if data['uphone'] not in user_list:  # 如果账户不存在，则添加进user列表,并重新保存cookie
                        dict = {}
                        dict[data['uphone']] = data['upwd']
                        user_list.append(dict)
                        list_str = json.dumps(user_list)
                        resp.set_cookie('user', list_str, 60 * 60 * 24 * 7)
                else:  # 如果cookie里没有存放数据的user,则添加user到cookie
                    user_list = []
                    dict = {}
                    dict[data['uphone']] = data['upwd']
                    user_list.append(dict)
                    list_str = json.dumps(user_list)
                    resp.set_cookie('user', list_str, 60 * 60 * 24 * 7)
            # 获取上一次页面路由next的值,再表单隐藏域中
            # 如果有next获取值，默认为'/'
            next2 = request.POST.get('next')
            return redirect(next2)
        else:
            return HttpResponse('登陆失败')


@login_required(login_url='/user/login/')
def logout(request):
    # 如果通过过get请求访问，
    if request.method == 'GET':
        # 执行auth中的logout函数
        # 将user和request对象解绑
        auth.logout(request)
        return redirect('/')


def modpwd(request):
    if request.method == 'GET':
        return render(request, 'user/personal_password.html')
    else:
        oldpwd = request.POST.get('upwd')
        newpwd = request.POST.get('npwd')
        newpwd2 = request.POST.get('rpwd')
        user = request.user
        if user.check_password(oldpwd):
            if not newpwd:
                msg = '新密码不能为空'
                return render(request, 'user/personal_password.html', locals())
            if newpwd != newpwd2:
                msg = '新密码两次输入不一致'
                return render(request, 'user/personal_password.html', locals())
            user.set_password(newpwd)
            user.save()
            return redirect('/')
        else:
            msg = '密码错误'
            return render(request, 'user/personal_password.html', locals())


def goods(request):
    if request.method == 'GET':
        return render(request, 'goods/product_list.html')
