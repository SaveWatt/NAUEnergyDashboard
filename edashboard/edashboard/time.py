from django import forms
from django.forms import ModelForm # EDIT: this import is needless
from django.forms.extras import SelectDateWidget

from .models import Hyuga_Requests


class HyugaRequestForm(forms.ModelForm):
    class Meta:
        model = Hyuga_Requests
        fields = ('reason', 's_date', 'e_date')
        widgets = {
            's_date': SelectDateWidget(),
            'e_date': SelectDateWidget(),
        }
