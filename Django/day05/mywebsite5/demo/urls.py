from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.demo_views),
    url(r'^post_views/$', views.post_views, name='post_view'),
    url(r'^get_views/$', views.get_views, name='get_view'),
    url(r'^remark/$', views.remark, name='remark'),
]
