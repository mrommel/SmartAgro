from django.conf.urls import include, url

from . import views
from django.contrib.auth import views as auth_views

#app_name = 'core'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    
    # data
    url(r'^data$', views.data, name='data'),
    
    # machines
    url(r'^machines$', views.machines, name='machines'),
    url(r'^machine/detail/(?P<machine_id>.+)$', views.machine_detail, name='machine_detail'),
    url(r'^machine/edit/(?P<machine_id>.+)$', views.machine_edit, name='machine_edit'),
    
    # persons
    url(r'^persons$', views.persons, name='persons'),
    url(r'^person/detail/(?P<person_id>.+)$', views.person_detail, name='person_detail'),
    url(r'^person/edit/(?P<person_id>.+)$', views.person_edit, name='person_edit'),
    
    # fields
    
    url(r'accounts/$', include('accounts.urls')), 
    
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]