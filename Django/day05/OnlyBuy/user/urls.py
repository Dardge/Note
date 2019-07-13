from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.user),
    url(r'^register/$', views.register2),
    # url(r'^login/$', views.login),
    url(r'^login/$', views.login2),
    url(r'^setcookie/$', views.setcookie),
    url(r'^getcookie/$', views.getcookie),
    url(r'^search/$', views.search_views),
    url(r'^modcookie/$', views.modcookie),
    url(r'^delcookie/$', views.delcookie),
    url(r'^setcookiechn/$', views.setcookiechn),
    url(r'^getcookiechn/$', views.getcookiechn),
]
