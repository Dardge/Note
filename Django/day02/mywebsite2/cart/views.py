from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import datetime


# Create your views here.
def index0(request):
    # # 通过loader获取模板
    # t = loader.get_template('index0.html')
    # # 将t转换成字符串
    # html = t.render()
    # # 响应给客户端
    # return HttpResponse(html)
    context = {'name': 'shibw'}
    return render(request, 'index0.html', context)


def var_views(request):
    str = '模板中的变量——字符串'
    num = 3306
    list = ['孙悟空', '猪八戒']
    tup = ('武松', '李逵')
    dict = {'BJ': '北京', 'SH': '上海'}

    def sayHai():
        return 'Hello,this is a view'

    say = sayHai()

    class Dog(object):
        name = '旺财'

        def eat(self):
            return '吃狗粮'

    dog = Dog()
    students = []
    return render(request, 'var.html', locals())


def filter_views(request):
    time = datetime.datetime.now()
    list = [1, 2, 3, 4, 5]
    dict = None
    return render(request, 'filter.html', locals())


def static(request):
    return render(request, 'load_static.html')


def index1(request):
    return render(request, 'index1.html')


def index(request):
    return render(request, 'index.html')


def base_views(request):
    return render(request, 'base_html.html')


def child_views(request):
    return render(request, 'child_html.html')
