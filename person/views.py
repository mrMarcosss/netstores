from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
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


def person_edit(request, pk):
    if pk != 'new':
        instance = get_object_or_404(Person, pk=pk)
    else:
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
