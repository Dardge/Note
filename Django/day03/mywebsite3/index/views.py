from .models import *
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def oto_views(request):
    # # 增加舒夫人到wife 表 关联老舍的数据
    # wife = Wife()
    # wife.name = '巴夫人'
    # wife.age = 20
    # # 通过wife表中author_id的属性找到对应的Author对象
    # # wife.author_id = 2
    # author = Author.objects.get(name='巴金')
    # wife.author = author
    # wife.save()
    # wife = Wife.objects.get(name='巴夫人')
    # print('夫人姓名：%s,作者姓名：%s' % (wife.name, wife.author.name))
    wife = Wife.objects.create(name='张夫人', age=29, author_id=9)
    return HttpResponse('增加%s成功' % wife.name)


def oto2_views(request):
    """
    :param request:
    :return:
    """
    wife_list = Wife.objects.all()
    author_list = Author.objects.all()
    return render(request, 'oto.html', locals())


def otm_views(request):
    """
    实现一对多的查询
    获取所有的图书，展示图书和对应的出版社
    获取所有的出版社，展示出版社的图书
    :param request:
    :return:
    """
    publisher = Publisher.objects.get(name='皮皮虾出版社')
    book_list = publisher.book_set.all()
    pub_list = Publisher.objects.all()
    return render(request, 'otm.html', locals())


def mtn_views(request):
    book = Book.objects.get(id=3)
    print(book.author.all())
    # 反向查询Author-->Book
    laoshe = Author.objects.get(name='张三')
    print(laoshe.book_set.all())
    return HttpResponse('查询完毕')
