from django.contrib import admin
from django.conf.urls import url
from .views import get_features, create_feature

urlpatterns = [
    url(r'^get_features', get_features, name='get_features'),
    url(r'^create_feature', create_feature, name='crate_feature'),
]