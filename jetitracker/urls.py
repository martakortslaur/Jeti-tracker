"""jetitracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import index, logout, login, registration, user_profile
from accounts import urls as accounts_urls
from bug.views import add_bug, show_bug, bug_description
from bug import urls as bug_urls
from features.views import create_feature, get_features
from features import urls as urls_features
from cart import urls as urls_cart
from checkout import urls as urls_checkout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^accounts/logout/$', logout, name="logout"),
    url(r'^accounts/login/$', login, name="login"),
    url(r'^accounts/register/$', registration, name="registration"),
    url(r'^accounts/profile/$', user_profile, name="profile"),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^bug/add_bug', add_bug, name="add_bug"),
    url(r'^bug/show_bug', show_bug, name="show_bug"),
    url(r'^bug/bug_description', bug_description, name="bug_description"),
    url(r'^bug/', include(bug_urls)),
    url(r'^features/create_feature', create_feature, name="create_feature"),
    url(r'^features/get_features', get_features, name="get_features"),
    url(r'^cart/', include(urls_cart)),
    url(r'^features/', include(urls_features)),
    url(r'^chekout/', include(urls_checkout)),
]