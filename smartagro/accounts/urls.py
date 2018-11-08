# accounts/urls.py
from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
]