from django.conf.urls import include, url

from . import views
from django.contrib.auth import views as auth_views

#app_name = 'core'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^machines$', views.machines, name='machines'),
    url(r'^machine/detail/(?P<machine_id>.+)$', views.machine_detail, name='machine_detail'),
    url(r'^machine/edit/(?P<machine_id>.+)$', views.machine_edit, name='machine_edit'),
    
    url(r'accounts/$', include('accounts.urls')), 
    
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]