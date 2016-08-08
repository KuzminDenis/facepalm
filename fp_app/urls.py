from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'), 
    url(r'^new/$', views.new, name='new'),
    url(r'^(?P<pk>[0-9]+)/$', views.details, name='details'), 
]