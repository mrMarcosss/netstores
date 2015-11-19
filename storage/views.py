from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, DeleteView
from storage.forms import Storage_editForm
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


def storage_edit(request, pk):
    if pk != 'new':
        instance = get_object_or_404(Storage, pk=pk)
    else:
        instance = None
    form = Storage_editForm(request.POST or None, instance=instance)
    if form.is_valid():
        saved_instance = form.save()
        if not instance:
            messages.success(request, u'Storage created successfully')
        else:
            messages.success(request, u'The storage saved successfully')
        return redirect('storage', pk=saved_instance.pk)
    return render(request, 'storage/storage_edit.html', {'form': form})


class StorageDelete(DeleteView):
    model = Storage
    success_url = reverse_lazy('storages')