from django.contrib import admin
from django.conf.urls import url
from .views import show_bug, bug_description, add_bug

urlpatterns = [
    url(r'^show_bug/(?P<id>[0-9]+)/', show_bug, name="show_bug"),
    url(r'^bug_description/(?P<id>[0-9]+)/', bug_description, name="bug_description"),
    url(r'^add_bug/', add_bug, name="add_bug"),
]
