from django.conf.urls import  url
from django.urls import include, path
from.import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'monitoring  '

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^detail$', views.detail, name='detail'),

    #url(r'^(?P<SOM_id>[0-9]+)/$', views.detail, name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)

