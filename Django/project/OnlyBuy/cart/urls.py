from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_all),
    url(r'^add/$', views.add_cart),
    url(r'^delete/(?P<id>\d+)/$', views.delete),
]
