from django.contrib import admin
from django.conf.urls import url
from .views import show_bug, bug_description, add_bug, toggle_status

urlpatterns = [
    url(r'^show_bug/(?P<id>[0-9]+)/', show_bug, name="show_bug"),
    url(r'^bug_description/(?P<id>\d+)$', bug_description, name="bug_description"),
    url(r'^add_bug/$', add_bug, name="add_bug"),
    url(r'^toggle/(?P<id>\d+)$', toggle_status)
]
