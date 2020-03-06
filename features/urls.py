from django.contrib import admin
from django.conf.urls import url, include
from .views import features, feature_description, add_or_edit_feature, delete_feature

urlpatterns = [
    url(r'^$', features, name='features'),
    url(r'^(?P<pk>\d+)/$', feature_description,
        name='feature_description'),
    url(r'^new/$', add_or_edit_feature, name='new_feature'),
    url(r'^(?P<pk>\d+)/edit/$', add_or_edit_feature,
        name="add_or_edit_feature"),
    url(r'^(?P<id>\d+)/delete/$', delete_feature,
        name="delete_feature"),
]

