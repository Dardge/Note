# @Time : 2019/6/6/11:11
# @Aufhor : Yang
# @File : views
# @Software : PyCharm

from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>这是我的第一个首页</h1>')


def index(request):
    return HttpResponse("request的请求路径：" + request.path)


def page1(request):
    return HttpResponse(request.method)


def page_year(request, year):
    # year对应正则表达式的第一个分组() 2015
    return HttpResponse('当前年份：' + year)


def date(request, year, month, day):
    return HttpResponse(year + "年" + month + "月" + day + "日")


def birthday(request, year, month, day):
    return HttpResponse("生日是：" + year + "年" + month + "月" + day + "日")


def students(request, name, age):
    return HttpResponse("学生姓名：" + name + "年龄：" + age)


def goods(request, id, shop):
    return HttpResponse("当前查看的是id为" + id + "的商品：" + shop)
