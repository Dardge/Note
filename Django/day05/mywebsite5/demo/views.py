from django.shortcuts import render
from django.http import HttpResponse
from .forms import *


# Create your views here.
def demo_views(request):
    print(request)
    body = request.body
    path = request.path
    scheme = request.scheme
    method = request.method
    method_get = request.GET
    method_post = request.POST
    cookies = request.COOKIES
    meta = request.META
    # return HttpResponse('响应完毕')
    return render(request, 'request_demo.html', locals())


def post_views(request):
    if request.method == 'GET':
        return render(request, 'post.html')
    else:
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        return HttpResponse('用户名：%s-->密码：%s' % (uname, pwd))


def get_views(request):
    # http://127.0.0.1:8000/demo/get_views/?gname=赵秉乾&gprice=2&count=3
    if request.method == 'GET':
        gname = request.GET.get('gname')
        gprice = request.GET.get('gprice')
        count = request.GET.get('count')
        sum_price = int(count) * int(gprice)
        return HttpResponse('<h1>您购买了%s个<span style="color: red">%s</span>%s毛钱</h1>' % (count, gname, sum_price))


def remark(request):
    form = RemarkForm()
    print(form)
    return render(request, 'remark_form.html', locals())
