from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^add_session/$', views.add_session),
    url(r'^mod_session/(?P<new>\d+)/$', views.mod_session),
    url(r'^del_session/$', views.del_session),
    url(r'^show_session/$', views.show_session),
    url(r'^get_views/$', views.get_views),
    url(r'^get_server/$', views.get_server),
    url(r'^post_views/$', views.post_views),
    url(r'^post_server/$', views.post_server),
    url(r'^show/$', views.show_view),
    url(r'^upload/$', views.upload),
    url(r'^upload_view/$', views.upload_view),
]

urlpatterns += []
