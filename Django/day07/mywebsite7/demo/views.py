from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST


# Create your views here.
def add_session(request):
    request.session['mysession'] = 100
    return HttpResponse('添加session成功')


def show_session(request):
    # mysession = request.session['mysession']
    mysession = request.session.get('mysession', '没有值')
    print('mysession:' + str(mysession), mysession)
    return HttpResponse('mysession:' + str(mysession))


def mod_session(request, new):
    request.session['mysession'] = new
    return HttpResponse('修改session成功<a href="/demo/show_session">去查询</a>')


def del_session(request):
    del request.session['mysession']
    return HttpResponse('删除session成功')


def get_views(request):
    return render(request, 'ajax-get.html')


def get_server(request):
    uname = request.GET.get('uname')
    uage = request.GET.get('uage')
    return HttpResponse('姓名：%s  年龄：%s' % (uname, uage))


def post_views(request):
    return render(request, 'ajax-post.html')


def post_server(request):
    uname = request.POST.get('uname')
    return HttpResponse('传递过来的数据为：%s' % uname)


def show_view(request):
    print('demo中的show_view视图')

    # raise ValueError('hehe')
    # return HttpResponse('OK')
    def render():
        print('in demo/render')
        return HttpResponse('098k')

    resp = HttpResponse('OK')
    resp.render = render
    return resp


def upload(request):
    return render(request, 'upload.html')


from django.conf import settings
import os


@require_POST
def upload_view(request):
    if request.method == 'POST':
        file = request.FILES['myfile']
        # file.name 文件名
        # file.file 文件数据
        filename = os.path.join(settings.MEDIA_ROOT, file.name)
        print(filename)
        with open(filename, 'wb') as f:
            f.write(file.file.read())
            return HttpResponse('文件接收成功')
    return HttpResponse('文件接收失败')
