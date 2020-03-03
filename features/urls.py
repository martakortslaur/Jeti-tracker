from django.contrib import admin
from django.conf.urls import url
from .views import get_features, create_feature, delete_feature

urlpatterns = [
    url(r'^get_features', get_features, name='get_features'),
    url(r'^create_feature', create_feature, name='create_feature'),
    url(r'^delete_feature', delete_feature, name='delete_feature'),
]

# from django.conf.urls import url
# from .views import feature, add_comment_feature, add_edit_feature, feature_detail, upvote_feature

# urlpatterns = [
#     url(r'^$', feature, name='feature'),
#     url(r'^feature_detail/(?P<id>\d+)/$', feature_detail, name='feature_detail'),
#     url(r'^edit_feature/(?P<id>\d+)/$', add_edit_feature, name='edit_feature'),
#     url(r'^add_feature/$', add_edit_feature, name='add_feature'),
#     url(r'^add_comment_feature/(?P<id>\d+)/$',
#         add_comment_feature, name='add_comment_feature'),
#     url(r'^upvote_feature/$', upvote_feature, name='upvote_feature'),
# ]