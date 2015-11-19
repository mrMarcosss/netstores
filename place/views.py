from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from place.forms import CountryEditForm, CityEditForm
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


class CountryUpdateView(UpdateView):
    form_class = CountryEditForm
    model = Country

    def form_valid(self, form):
        messages.success(self.request, u'Country saved successfully')
        return super(CountryUpdateView, self).form_valid(form)


class CityUpdateView(UpdateView):
    form_class = CityEditForm
    model = City

    def form_valid(self, form):
        messages.success(self.request, u'City saved successfully')
        return super(CityUpdateView, self).form_valid(form)


class CountryCreateView(CreateView):
    form_class = CountryEditForm
    model = Country

    def form_valid(self, form):
        messages.success(self.request, u'Country created successfully')
        return super(CountryCreateView, self).form_valid(form)


class CityCreateView(CreateView):
    form_class = CityEditForm
    model = City

    def form_valid(self, form):
        messages.success(self.request, u'City created successfully')
        return super(CityCreateView, self).form_valid(form)


class CityDelete(DeleteView):
    model = City
    success_url = reverse_lazy('cities')


class CountryDelete(DeleteView):
    model = Country
    success_url = reverse_lazy('countries')