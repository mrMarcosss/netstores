from django.conf.urls import url
from person.views import PersonsListView, PersonDetailView

urlpatterns = [
    url(r'^persons/$', PersonsListView.as_view(), name='persons'),
    url(r'^person/(?P<pk>\d+)/$', PersonDetailView.as_view(), name='person'),
]