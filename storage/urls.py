from django.conf.urls import url
from storage.views import StoragesListView, StorageDetailView, StorageDelete
from . import views

urlpatterns = [
    url(r'^storages/$', StoragesListView.as_view(), name='storages'),
    url(r'^storage/(?P<pk>\d+)/$', StorageDetailView.as_view(), name='storage'),
    url(r'^storage/edit/(?P<pk>\d+|new)/$', views.storage_edit, name='storage_edit'),
    url(r'^storage/delete/(?P<pk>\d+)/$', StorageDelete.as_view(), name='storage_delete'),
]