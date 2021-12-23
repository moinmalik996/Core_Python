from django import forms
from django.forms.widgets import PasswordInput


class StudentDataCollection(forms.Form):
    name      = forms.CharField(max_length=70)
    email     = forms.EmailField(max_length=70)
    password  = forms.CharField(widget=forms.PasswordInput)

