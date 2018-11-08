from django.conf.urls import include, url

from . import views
from django.contrib.auth import views as auth_views

#app_name = 'core'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    #url(r'^index$', views.index, name='index'),
    
    url(r'accounts/$', include('accounts.urls')), 
    
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]