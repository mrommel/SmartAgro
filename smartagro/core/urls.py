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
    url(r'^fields$', views.fields, name='fields'),
    
    # documentations
    #url(r'^documentations$', views.documentations, name='documentations'),
    url(r'^documentations$', views.DocumentationList.as_view(), name='documentation_list'),
    url(r'^documentation/add$', views.DocumentationCreate.as_view(), name='documentation_add'),
    url(r'^documentation/detail/(?P<documentation_id>.+)/$', views.documentation_detail, name='documentation_detail'),
    url(r'^documentation/edit/(?P<documentation_id>.+)$', views.DocumentationUpdate.as_view(), name='documentation_edit'),
    url(r'^documentation/delete/(?P<documentation_id>.+)$', views.DocumentationDelete.as_view(), name='documentation_delete'),
    
    url(r'accounts/$', include('accounts.urls')),     
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]