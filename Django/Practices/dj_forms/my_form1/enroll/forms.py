from django import forms
from django.forms.widgets import EmailInput, PasswordInput, TextInput  # import forms class


#create a Particular Form


class StudentsRegistration(forms.Form):
    name = forms.CharField(widget=TextInput())
    email = forms.EmailField(widget=EmailInput())
    password = forms.CharField(widget=PasswordInput())
