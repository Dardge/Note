from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^oto/$', views.oto_views),
    url(r'^oto2/$', views.oto2_views),
    url(r'^otm/$', views.otm_views),
    url(r'^mtn/$', views.mtn_views),
]
