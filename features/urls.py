from django.conf.urls import url, include
from .views import features

urlpatterns = [
    url(r'^$', features, name='features'),
]