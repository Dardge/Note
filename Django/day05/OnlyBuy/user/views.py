from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *
import json


# Create your views here.
def user(request):
    # return render(request, 'user/index.html')
    return render(request, 'user/login.html')


def register2(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    else:
        uname = request.POST.get('uname')
        upwd = request.POST.get('upwd')
        uphone = request.POST.get('uphone')
        uemail = request.POST.get('uemail')
        isActive = 1 if request.POST.get('isActive') else 0
        User.objects.create(uname=uname, upwd=upwd, uphone=uphone, uemail=uemail, isActive=isActive)
        return HttpResponse('<h1>注册成功<h1>' + "<h1><a href='/user/'>返回user首页</a></h1>")


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'user/register1.html', locals())
    else:
        # uname = request.POST.get('uname')
        # upwd = request.POST.get('upwd')
        # uphone = request.POST.get('uphone')
        # uemail = request.POST.get('uemail')
        # isActive = 1 if request.POST.get('isActive') else 0
        form = RegisterForm(request.POST)
        # print(form)
        if form.is_valid():
            data = form.cleaned_data
            print(data)  # 返回字典格式的数据
            user = User(**data)
            try:
                user.save()
            except Exception as e:
                return HttpResponse('<p>注册失败==>%s</p><a href="/user/register/">重新注册</a>' % e)
        # try:
        #     User.objects.create(uname=uname, upwd=upwd, uphone=uphone, uemail=uemail, isActive=isActive)
        # except Exception as e:
        #     print(e)
        #     return HttpResponse('注册失败==>%s' % e)
        return HttpResponse('<h1>注册成功<h1>' + "<h1><a href='/user/'>返回user首页</a></h1>")


def login2(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    else:
        data = request.POST
        user = User.objects.filter(uphone=data['uphone']).first()
        if not user:  # 如果此用户不存在
            login_form = LoginForm()
            text = '用户不存在'
            return render(request, 'user/login_form.html', locals())
        if data['upwd'] == user.upwd:  # 如果密码正确
            resp = HttpResponse('登陆成功')
            if request.session['verifycode'] == request.POST.get('ma'):
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
                return resp
            return HttpResponse('验证吗错误')
        else:
            return HttpResponse('登陆失败')


def login(request):
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'user/login_form.html', locals())
    else:
        data = request.POST
        user = User.objects.filter(uphone=data['uphone']).first()
        if not user:  # 如果此用户不存在
            login_form = LoginForm()
            text = '用户不存在'
            return render(request, 'user/login_form.html', locals())
        if data['upwd'] == user.upwd:  # 如果密码正确
            resp = HttpResponse('登陆成功')
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
            return resp
        else:
            login_form = LoginForm()
            text = '密码错误'
            return render(request, 'user/login_form.html', locals())


def setcookie(request):
    resp = HttpResponse('增加cookies成功')
    resp.set_cookie('uname', 'laowang', 60 * 60)
    return resp


def getcookie(request):
    cookies = request.COOKIES
    print(cookies)
    return HttpResponse('获取cookie成功')


def search_views(request):
    if request.method == 'GET':
        # 判断kw在不在GET中
        # if 'kw' in request.GET:
        if request.GET.get('kw'):
            kw = request.GET.get('kw')
            detail = '与《%s》相关的内容' % kw
            # 判断cookie中是否有kw
            if 'kw_list' in request.COOKIES:
                kw_list = request.COOKIES['kw_list']
                kw_list = json.loads(kw_list)
                resp = render(request, 'user/search.html', locals())
                if kw in kw_list:
                    return resp
                # 如果kw_list中不存在kw则保存
                kw_list.append(kw)
                list_str = json.dumps(kw_list)
                resp = render(request, 'user/search.html', locals())
                resp.set_cookie('kw_list', list_str, 60 * 60 * 24 * 7)
                return resp
            else:
                kw_list = []
                kw_list.append(kw)
                list_str = json.dumps(kw_list)
                resp = render(request, 'user/search.html', locals())
                resp = render(request, 'user/search.html')
                resp.set_cookie('kw_list', list_str, 60 * 60 * 24 * 7)
                return resp
        else:
            # 无论是否有查询关键词，都要显示数据
            if 'kw_list' in request.COOKIES:
                kw_list = json.loads(request.COOKIES['kw_list'])
            resp = render(request, 'user/search.html', locals())
            return resp


def modcookie(request):
    resp = HttpResponse('将老王的生日修改为1999-12-25')
    resp.set_cookie('birthday', '1999-12-25', 3600)
    return resp


def delcookie(request):
    resp = HttpResponse('删除cookie laowang')
    resp.delete_cookie('uname')
    return resp


def setcookiechn(request):
    resp = HttpResponse('设置中文cookie成功')
    uname = '老王'
    # 借助json将uname的值转码存到cookie
    uname = json.dumps(uname)
    resp.set_cookie('uname', uname, 3600)
    # print(request.COOKIES['uname'])
    return resp


def getcookiechn(request):
    resp = HttpResponse('获取中文cookie成功')
    uname = request.COOKIES['uname']
    uname = json.loads(uname)
    print(uname)
    return resp
