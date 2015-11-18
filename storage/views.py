from django.shortcuts import render
from django.views.generic import ListView, DetailView

from storage.models import Storage


class StoragesListView(ListView):
    model = Storage


class StorageDetailView(DetailView):
    model = Storage

    def get_context_data(self, **kwargs):
            context = super(StorageDetailView, self).get_context_data(**kwargs)
            storage = super(StorageDetailView, self).get_object()
            context['stores'] = storage.store_set.all()
            return context