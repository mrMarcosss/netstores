from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
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


@login_required
def storage_edit(request, pk):
    if pk != 'new':
        if not request.user.has_perm('storage.change_storage'):
            raise PermissionDenied
        instance = get_object_or_404(Storage, pk=pk)
    else:
        if not request.user.has_perm('storage.add_storage'):
            raise PermissionDenied
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

    @method_decorator(permission_required('storage.delete_storage', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        return super(StorageDelete, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        response = super(StorageDelete, self).delete(request, *args, **kwargs)
        messages.success(request, u'Storage deleted successfully')
        return response