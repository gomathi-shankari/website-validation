from validation2app.models import link
from django import forms

class linkform(forms.ModelForm):
    class Meta:
        model = link
        fields="__all__"