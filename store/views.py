from django.shortcuts import render
from django.views.generic import ListView, DetailView
from store.models import Store, TypeOfStore


class StoresListView(ListView):
    model = Store


class TypesListView(ListView):
    model = TypeOfStore


class StoreDetailView(DetailView):
    model = Store

    def get_context_data(self, **kwargs):
            context = super(StoreDetailView, self).get_context_data(**kwargs)
            store = super(StoreDetailView, self).get_object()
            context['sellers'] = store.sellers.all()
            context['storages'] = store.storage.all()
            return context


class TypeDetailView(DetailView):
    model = TypeOfStore
