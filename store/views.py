from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, TemplateView, DeleteView
from store.forms import StoreEditForm, TypeEditForm
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


class StoreEditView(TemplateView):
    template_name = 'store/store_edit.html'

    @method_decorator(permission_required('store.change_store', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        if kwargs['pk'] != 'new':
            self.instance = get_object_or_404(Store, pk=kwargs['pk'])
        else:
            self.instance = None
        self.form = StoreEditForm(request.POST or None, instance=self.instance)
        return super(StoreEditView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(StoreEditView, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        if self.form.is_valid():
            saved_instance = self.form.save()
            if not self.instance:
                messages.success(request, u'The store created successfully')
            else:
                messages.success(request, u'The store saved successfully')
            return redirect('store', pk=saved_instance.pk)
        return self.get(request, *args, **kwargs)


class TypeEditView(TemplateView):
    template_name = 'store/type_edit.html'

    @method_decorator(permission_required('typeofstore.change_typeofstore', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        if kwargs['pk'] != 'new':
            self.instance = get_object_or_404(TypeOfStore, pk=kwargs['pk'])
        else:
            self.instance = None
        self.form = TypeEditForm(request.POST or None, instance=self.instance)
        return super(TypeEditView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TypeEditView, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        if self.form.is_valid():
            saved_instance = self.form.save()
            if not self.instance:
                messages.success(request, u'Type created successfully')
            else:
                messages.success(request, u'Type saved successfully')
            return redirect('type', pk=saved_instance.pk)
        return self.get(request, *args, **kwargs)


class StoreDelete(DeleteView):
    model = Store
    success_url = reverse_lazy('stores')

    @method_decorator(permission_required('store.delete_store', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        return super(StoreDelete, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        response = super(StoreDelete, self).delete(request, *args, **kwargs)
        messages.success(request, u'Store deleted successfully')
        return response


class TypeDelete(DeleteView):
    model = TypeOfStore
    success_url = reverse_lazy('types')

    @method_decorator(permission_required('typeofstore.delete_typeofstore', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        return super(TypeDelete, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        response = super(TypeDelete, self).delete(request, *args, **kwargs)
        messages.success(request, u'Type of store deleted successfully')
        return response
