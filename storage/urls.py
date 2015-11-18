from django.conf.urls import url
from storage.views import StoragesListView, StorageDetailView

urlpatterns = [
    url(r'^storages/$', StoragesListView.as_view(), name='storages'),
    url(r'^storage/(?P<pk>\d+)/$', StorageDetailView.as_view(), name='storage'),
]