from django import forms
from netstores.forms import BootstrapFormMixin
from storage.models import Storage


class Storage_editForm(forms.ModelForm, BootstrapFormMixin):
    class Meta:
        model = Storage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Storage_editForm, self).__init__(*args, **kwargs)
        BootstrapFormMixin.__init__(self)