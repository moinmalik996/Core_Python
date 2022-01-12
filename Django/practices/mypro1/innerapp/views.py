from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import Group
# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            user = fm.save()
            group = Group.objects.get(name='Editor')
            user.groups.add(group)
        
    else:
        fm = UserCreationForm()
    return render(request, 'innerapp/signup.html', {'form':fm})


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
                    return HttpResponseRedirect('/dashBoard/')
        else:
            fm = AuthenticationForm()


        return render(request, 'innerapp/login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/dashBoard/')


def get_dashBoard(request):
    if request.user.is_authenticated:
        return render(request, 'innerapp/dashBoard.html', {'name':request.user})
    else:
        return HttpResponseRedirect('/login/')



def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')



