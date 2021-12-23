from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect

#import models class
from .models import StudentData

 # import forms class
from .forms import Registration


# Create your views here.

def thankyou(request):
    return render(request, 'enrollment/thankyou.html')


def collect_data_func(request):

    if request.method == 'POST':
        sdc = Registration(request.POST)

        if sdc.is_valid():
            name_f = sdc.cleaned_data['name']
            email_f = sdc.cleaned_data['email']
            password_f = sdc.cleaned_data['password']

            print('Name      :', name_f)
            print('Email     :', email_f)
            print('Password  :', password_f)

            reg = StudentData(name=name_f, email= email_f, password=password_f)
            reg.save()

            # rem = StudentData(id=2)
            # rem.delete()

            return HttpResponseRedirect('/student/thankyou')
        else:
            return render(request, 'enrollment/data_upload.html', {'form': sdc})
    else:
        sdc = Registration()
        return render(request, 'enrollment/data_upload.html', {'form': sdc})
