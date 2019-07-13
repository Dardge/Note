from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<id>\d+)$', views.question),
    url(r'^/(?P<id>\d+)/result/$', views.result)
]
