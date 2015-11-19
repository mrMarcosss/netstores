from django import forms

from netstores.forms import BootstrapFormMixin
from place.models import Country, City


class CountryEditForm(forms.ModelForm, BootstrapFormMixin):
    class Meta:
        model = Country
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CountryEditForm, self).__init__(*args, **kwargs)
        BootstrapFormMixin.__init__(self)


class CityEditForm(forms.ModelForm, BootstrapFormMixin):
    class Meta:
        model = City
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CityEditForm, self).__init__(*args, **kwargs)
        BootstrapFormMixin.__init__(self)