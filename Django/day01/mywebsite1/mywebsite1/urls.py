"""mywebsite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^page1/$', views.page1),
    url(r'^index/$', views.index),
    url(r'^year/(\d{4})$', views.page_year),  # http://127.0.0.1:8000/year/2015
    url(r'^date/(\d{4})/(\d+)/(\d+)$', views.date),  # http://127.0.0.1:8000/date/2015/1/25
    url(r'^birthday/(\d{4})/(\d{1,2})/(\d{1,2})$', views.birthday),  # http://127.0.0.1:8000/birthday/2015/01/3
    # url(r'^students/(?P<name>\w+)/(?P<age>\d{1,2})$', views.students),
    url(r'^students/$', views.students, {'name': "盖伦", "age": '35'}),
    url(r'^goods/(?P<id>\d+)$', views.goods, {"shop": "无尽之刃"}),
    url(r'^music/', include('music.urls')),
]
