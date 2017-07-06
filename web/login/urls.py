from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^empview/$', views.detailsCreate.as_view(), name='emp-add'),
    url(r'^adminview/$', views.ad, name='ad'),
    url(r'^adminview/(?P<id>[0-9]+)/$', views.emp, name='emp'),
    url(r'^admindelete/(?P<id>[0-9]+)/$', views.empdel, name='empdel'),
]
