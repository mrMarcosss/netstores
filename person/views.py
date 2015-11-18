from django.views.generic import ListView, DetailView

from person.models import Person
from store.models import Store


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
