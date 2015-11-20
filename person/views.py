from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from person.forms import PersonEditForm
from person.models import Person


class PersonsListView(ListView):
    model = Person


class PersonDetailView(DetailView):
    model = Person

    def get_context_data(self, **kwargs):
            context = super(PersonDetailView, self).get_context_data(**kwargs)
            person = super(PersonDetailView, self).get_object()
            context['own_store'] = person.own_store.all()
            context['seller_in'] = person.seller_in.all()
            return context


@login_required
def person_edit(request, pk):
    if pk != 'new':
        if not request.user.has_perm('person.change_person'):
            raise PermissionDenied
        instance = get_object_or_404(Person, pk=pk)
    else:
        if not request.user.has_perm('person.add_person'):
            raise PermissionDenied
        instance = None
    form = PersonEditForm(request.POST or None, instance=instance)
    if form.is_valid():
        saved_instance = form.save()
        if not instance:
            messages.success(request, u'Person created successfully')
        else:
            messages.success(request, u'The person saved successfully')
        return redirect('person', pk=saved_instance.pk)
    return render(request, 'person/person_edit.html', {'form': form})


class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('persons')

    @method_decorator(permission_required('person.delete_person', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        return super(PersonDelete, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        response = super(PersonDelete, self).delete(request, *args, **kwargs)
        messages.success(request, u'Person deleted successfully')
        return response
