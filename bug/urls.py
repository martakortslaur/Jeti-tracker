from django.contrib import admin
from django.conf.urls import url
from .views import show_bug, bug_description, add_bug, toggle_status, add_comment_bug
from .views import allbugs

urlpatterns = [
    url(r'^$', allbugs, name='allbugs'),
    url(r'^show_bug/(?P<id>\d+)/$', show_bug, name="show_bug"),
    url(r'^bug_description/(?P<id>\d+)/$',
        bug_description, name="bug_description"),
    url(r'^add_bug/$', add_bug, name="add_bug"),
    url(r'^toggle/(?P<id>\d+)$', toggle_status),   
    url(r'^add_comment_bug/(?P<id>\d+)/$',
        add_comment_bug, name='add_comment_bug'),
]
