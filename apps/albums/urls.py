# Author Luis Manuel Gutierrez http://luismanu.com
from django.conf.urls import url

from .views import AlbumDetail, AlbumCreate, AlbumList, AlbumUpdate, AlbumDelete

urlpatterns = [
    url(r'^albums/$', AlbumList.as_view(), name='album_list'),
    url(r'^albums/(?P<pk>[0-9]+)/$', AlbumDetail.as_view(), name='album_detail'),
    url(r'^albums/add/$', AlbumCreate.as_view(), name='album_create'),
    url(r'^albums/update/(?P<pk>[0-9]+)/$', AlbumUpdate.as_view(), name='album_update'),
    url(r'^albums/delete/(?P<pk>[0-9]+)/$', AlbumDelete.as_view(), name='album_delete')
]