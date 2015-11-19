from django.conf.urls import url
from store.views import StoresListView, StoreDetailView, TypesListView, TypeDetailView, StoreEditView, TypeEditView, \
    StoreDelete, TypeDelete

urlpatterns = [
    url(r'^stores/$', StoresListView.as_view(), name='stores'),
    url(r'^types/$', TypesListView.as_view(), name='types'),
    url(r'^store/(?P<pk>\d+)/$', StoreDetailView.as_view(), name='store'),
    url(r'^store/edit/(?P<pk>\d+|new)/$', StoreEditView.as_view(), name='store_edit'),
    url(r'^type/(?P<pk>\d+)/$', TypeDetailView.as_view(), name='type'),
    url(r'^type/edit/(?P<pk>\d+|new)/$', TypeEditView.as_view(), name='type_edit'),
    url(r'^store/delete/(?P<pk>\d+)/$', StoreDelete.as_view(), name='store_delete'),
    url(r'^type/delete/(?P<pk>\d+)/$', TypeDelete.as_view(), name='type_delete'),
]