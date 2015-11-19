from django import forms
from netstores.forms import BootstrapFormMixin
from store.models import Store, TypeOfStore


class StoreEditForm(forms.ModelForm, BootstrapFormMixin):
    class Meta:
        model = Store
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StoreEditForm, self).__init__(*args, **kwargs)
        BootstrapFormMixin.__init__(self)


class TypeEditForm(forms.ModelForm, BootstrapFormMixin):
    class Meta:
        model = TypeOfStore
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TypeEditForm, self).__init__(*args, **kwargs)
        BootstrapFormMixin.__init__(self)
