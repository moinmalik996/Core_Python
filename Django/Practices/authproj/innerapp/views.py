from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
        
    else:
        fm = UserCreationForm()
    return render(request, 'enroll/signup.html', {'form':fm})


def login_form(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            pword = fm.cleaned_data['password']

            user = authenticate(username=uname, password=pword)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile/')
    else:
        fm = AuthenticationForm()


    return render(request, 'enroll/login.html', {'form':fm})


def get_profile(request):
    return render(request, 'enroll/profile.html')