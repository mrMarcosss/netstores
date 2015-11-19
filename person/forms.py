from django import forms
from django.forms.extras import SelectDateWidget
from netstores.forms import BootstrapFormMixin
from person.models import Person


class PersonEditForm(forms.ModelForm, BootstrapFormMixin):

    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PersonEditForm, self).__init__(*args, **kwargs)
        self.fields['birth_date'].widget = SelectDateWidget(years=range(1950, 2010))
        BootstrapFormMixin.__init__(self)
