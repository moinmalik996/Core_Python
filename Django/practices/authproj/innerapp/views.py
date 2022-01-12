from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
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
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                pword = fm.cleaned_data['password']

                user = authenticate(username=uname, password=pword)
                if user is not None:
                    messages.success(request, 'Logged In Successfully')
                    login(request, user)
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()


        return render(request, 'enroll/login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/profile/')


def get_profile(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/profile.html', {'name':request.user})
    else:
        return HttpResponseRedirect('/login/')



def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')



def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'enroll/changePass.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')