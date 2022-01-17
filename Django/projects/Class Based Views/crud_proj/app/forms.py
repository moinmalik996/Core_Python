from django.core import validators
from django import forms
from .models import StudentData

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = StudentData
        fields = ['name', 'email', 'pass_w']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'pass_w': forms.PasswordInput(attrs={'class':'form-control'})
        }
        labels = {
            'name': 'Enter Your Name',
            'email': 'Enter Your Email',
            'pass_w': 'Enter Your Password'
        }