from django.conf.urls import include, url

from . import views

#app_name = 'core'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    
    # data
    url(r'^data$', views.data, name='data'),
    
    # machines
    url(r'^machines$', views.MachineList.as_view(), name='machine_list'),
    url(r'^machine/add$', views.MachineCreate.as_view(), name='machine_add'),
    url(r'^machine/detail/(?P<machine_id>.+)$', views.MachineDetail.as_view(), name='machine_detail'),
    url(r'^machine/edit/(?P<machine_id>.+)$', views.MachineUpdate.as_view(), name='machine_edit'),
    url(r'^machine/delete/(?P<machine_id>.+)$', views.MachineDelete.as_view(), name='machine_delete'),
    
    # persons
    url(r'^persons$', views.PersonList.as_view(), name='person_list'),
    url(r'^person/add$', views.PersonCreate.as_view(), name='person_add'),
    url(r'^person/detail/(?P<person_id>.+)$', views.PersonDetail.as_view(), name='person_detail'),
    url(r'^person/edit/(?P<person_id>.+)$', views.PersonUpdate.as_view(), name='person_edit'),
    url(r'^person/delete/(?P<person_id>.+)$', views.PersonDelete.as_view(), name='person_delete'),
    
    # fields
    url(r'^fields$', views.FieldList.as_view(), name='field_list'),
    url(r'^field/add$', views.FieldCreate.as_view(), name='field_add'),
    url(r'^field/detail/(?P<field_id>.+)/$', views.FieldDetail.as_view(), name='field_detail'),
    url(r'^field/edit/(?P<field_id>.+)$', views.FieldUpdate.as_view(), name='field_edit'),
    url(r'^field/delete/(?P<field_id>.+)$', views.FieldDelete.as_view(), name='field_delete'),
    
    # fertilizers
    url(r'^fertilizers$', views.FertilizerList.as_view(), name='fertilizer_list'),
    url(r'^fertilizer_activate$', views.fertilizer_activate, name='fertilizer_activate'),
    url(r'^fertilizer/detail/(?P<fertilizer_id>.+)/$', views.FertilizerDetail.as_view(), name='fertilizer_detail'),
    
    # plant protectants
    url(r'^plantprotectants$', views.PlantProtectantList.as_view(), name='plant_protectant_list'),
    url(r'^plantprotectant_activate$', views.plantprotectant_activate, name='plant_protectant_activate'),
    url(r'^plantprotectant/detail/(?P<plant_protectant_id>.+)/$', views.PlantProtectantDetail.as_view(), name='plant_protectant_detail'),
    
    # 
    url(r'^seeds$', views.SeedList.as_view(), name='seed_list'),
    url(r'^seed_activate$', views.seed_activate, name='seed_activate'),
    url(r'^seed/detail/(?P<seed_id>.+)/$', views.SeedDetail.as_view(), name='seed_detail'),
    
    # documentations
    url(r'^documentations$', views.DocumentationList.as_view(), name='documentation_list'),
    url(r'^documentation/add$', views.DocumentationCreate.as_view(), name='documentation_add'),
    url(r'^documentation/detail/(?P<documentation_id>.+)/$', views.DocumentationDetail.as_view(), name='documentation_detail'),
    url(r'^documentation/edit/(?P<documentation_id>.+)$', views.DocumentationUpdate.as_view(), name='documentation_edit'),
    url(r'^documentation/delete/(?P<documentation_id>.+)$', views.DocumentationDelete.as_view(), name='documentation_delete'),
    
    url(r'^accounts/', include('accounts.urls')),     
]