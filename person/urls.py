from django.conf.urls import url
from person.views import PersonsListView, PersonDetailView, PersonDelete
from . import views

urlpatterns = [
    url(r'^persons/$', PersonsListView.as_view(), name='persons'),
    url(r'^person/(?P<pk>\d+)/$', PersonDetailView.as_view(), name='person'),
    url(r'^person/edit/(?P<pk>\d+|new)/$', views.person_edit, name='person_edit'),
    url(r'^person/delete/(?P<pk>\d+)/$', PersonDelete.as_view(), name='person_delete'),
]