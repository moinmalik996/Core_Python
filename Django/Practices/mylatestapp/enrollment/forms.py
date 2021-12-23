from django import forms
from django.forms import widgets
from .models import StudentData

class Registration(forms.ModelForm):
    class Meta:
        model = StudentData
        fields = ['name', 'email', 'password']
        labels = {'name': 'Enter Your Name :',
                  'email': 'Enter Your Email :',
                  'password': 'Enter Your Password:'}

        error_messages = {
            'name'     : {'required':'Name is Required'},
            'email'    : {'required':'Email is Required'},
            'password' : {'required':'Password is required'}
        }

        widgets = {'password': forms.PasswordInput}




