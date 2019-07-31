from django import forms

from .models import Pdfreport


class PdfreportForm(forms.ModelForm):
    class Meta:
        model = Pdfreport
        fields = ('title', 'pdf')