from django.conf.urls import url
from place.views import CountriesListView, CitiesListView, CountryDetailView, CityDetailView, CountryUpdateView, \
    CityUpdateView, CountryCreateView, CityCreateView, CityDelete, CountryDelete

urlpatterns = [
    url(r'^countries/$', CountriesListView.as_view(), name='countries'),
    url(r'^country/(?P<pk>\d+)/$', CountryDetailView.as_view(), name='country'),
    url(r'^cities/$', CitiesListView.as_view(), name='cities'),
    url(r'^city/(?P<pk>\d+)/$', CityDetailView.as_view(), name='city'),
    url(r'^country/edit/(?P<pk>\d+)/$', CountryUpdateView.as_view(), name='country_edit'),
    url(r'^city/edit/(?P<pk>\d+)/$', CityUpdateView.as_view(), name='city_edit'),
    url(r'^country/edit/(?P<pk>new)/$', CountryCreateView.as_view(), name='country_create'),
    url(r'^city/edit/(?P<pk>new)/$', CityCreateView.as_view(), name='city_create'),
    url(r'^city/delete/(?P<pk>\d+)/$', CityDelete.as_view(), name='city_delete'),
    url(r'^country/delete/(?P<pk>\d+)/$', CountryDelete.as_view(), name='country_delete'),
]