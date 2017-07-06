from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from . import views

urlpatterns = [
	url(r'^$', views.index1, name='index1'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include('login.urls')),
]




#if settings.DEBUG:
	#urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
	#urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)