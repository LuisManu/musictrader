# Author Luis Manuel Gutierrez http://luismanu.com
from django.conf.urls import include, url
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import user_passes_test

from .views import ProfileDetailView, custom_registration, dashboard, UserUpdate




login_forbidden =  user_passes_test(lambda u: u.is_anonymous(), '/')

urlpatterns = [
	url(r'^profiles/(?P<pk>[0-9]+)/$', ProfileDetailView.as_view(), name='profile_detail'),
	url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^register/$', custom_registration, name='register'),
    url(r'^login/$', login_forbidden(login), name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}),
    url(r'^settings/$', UserUpdate.as_view(), name='settings'),
    url(r'^', include('django.contrib.auth.urls')),
]