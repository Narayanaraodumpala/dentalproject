from django import forms
from .models import DoctorsModel

class Doctorsform(forms.ModelForm):
    class Meta:
        model=DoctorsModel
        fields="__all__"