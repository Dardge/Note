# @Time : 2019/6/6/15:36
# @Aufhor : Yang
# @File : url
# @Software : PyCharm


from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index)
]
