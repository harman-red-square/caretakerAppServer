from django.conf.urls import include, url
from settings.NetworkConnectivity import views
##from django.conf.urls import url
##from settings import views

urlpatterns = [
    url(r'^settings/$', views.settings_list),
    url(r'^settings/(?P<pk>[0-9]+)/$', views.settings_detail),
]