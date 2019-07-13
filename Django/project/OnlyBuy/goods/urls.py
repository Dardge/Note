from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.goods_list),
    url(r'^list/(?P<type_id>\d+)$', views.goods_list),
    url(r'^detail/(?P<goods_id>\d+)$', views.detail),
    url(r'^detail/(?P<goods_id>\d+)/(?P<spec_id>\d+)$', views.detail),
]
