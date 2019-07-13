from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('投票应用首页')


def question(request, id):
    return HttpResponse(id + '号问题')


def result(rquest, id, result):
    return HttpResponse(id + '号问题内容是：' + result)
