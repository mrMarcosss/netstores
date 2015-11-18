from django.conf.urls import url

from place.views import CountriesListView, CitiesListView, CountryDetailView, CityDetailView

urlpatterns = [
    url(r'^countries/$', CountriesListView.as_view(), name='countries'),
    url(r'^country/(?P<pk>\d+)/$', CountryDetailView.as_view(), name='country'),
    url(r'^cities/$', CitiesListView.as_view(), name='cities'),
    url(r'^city/(?P<pk>\d+)/$', CityDetailView.as_view(), name='city'),
]