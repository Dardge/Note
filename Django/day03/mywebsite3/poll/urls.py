from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<id>\d+)/$', views.detail),
    url(r'^vote/$', views.vote, name='vote'),
    url(r'^(?P<answer_id>\d+)/result/$', views.result)
]
