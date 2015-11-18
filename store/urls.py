from django.conf.urls import url
from store.views import StoresListView, StoreDetailView, TypesListView, TypeDetailView

urlpatterns = [
    url(r'^stores/$', StoresListView.as_view(), name='stores'),
    url(r'^types/$', TypesListView.as_view(), name='types'),
    url(r'^store/(?P<pk>\d+)/$', StoreDetailView.as_view(), name='store'),
    url(r'^type/(?P<pk>\d+)/$', TypeDetailView.as_view(), name='type'),
]