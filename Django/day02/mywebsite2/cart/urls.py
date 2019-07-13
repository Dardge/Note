from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index0),
    url(r'^var', views.var_views),
    url(r'^filter', views.filter_views),
    url(r'^static', views.static),
    url(r'^index1', views.index1),
    url(r'^index', views.index),
    url(r'^base', views.base_views, name='base'),
    url(r'^child', views.child_views),
]
