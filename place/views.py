from django.shortcuts import render
from django.views.generic import ListView, DetailView

from place.models import Country, City


class CountriesListView(ListView):
    model = Country


class CitiesListView(ListView):
    model = City


class CountryDetailView(DetailView):
    model = Country

    def get_context_data(self, **kwargs):
        context = super(CountryDetailView, self).get_context_data(**kwargs)
        country = super(CountryDetailView, self).get_object()
        context['cities'] = country.city_set.all()
        return context


class CityDetailView(DetailView):
    model = City