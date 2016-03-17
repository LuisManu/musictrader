# Author Luis Manuel Gutierrez http://luismanu.com
from django.conf.urls import url

from .views import ArtistCreate, ArtistListView, ArtistDetailView, GenreCreate

urlpatterns = [
    url(r'^artists/$', ArtistListView.as_view(), name='artist_list'),
    url(r'^artists/(?P<pk>[0-9]+)/$', ArtistDetailView.as_view(), name='artist_detail'),
    url(r'^artists/add/$', ArtistCreate.as_view(), name='artist_create'),
    url(r'^artists/genre/add/$', GenreCreate.as_view(), name='genre_create')
]