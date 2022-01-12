from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SignUpForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.urls import reverse

# Create your views here.


# home_view
def home_view(request):
    post = Post.objects.all()
    return render(request, 'blogapp/home.html', {'posts':post})


def about_view(request):
    return render(request, 'blogapp/aboutus.html')

def contact_view(request):
    return render(request, 'blogapp/contact.html')

def dash_view(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        ip = request.session.get('ip', 0)
        return render(request, 'blogapp/dashboard.html', {'posts':posts, 
                                                          'fname':full_name,
                                                          'groups':gps,
                                                          'ip':ip })
    else:
        return HttpResponseRedirect('/login/')

def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("user",user,type(user))
            messages.success(request, "Congratulations! You have become an Author")
            group = Group.objects.get(name='Author')
            print("group---",group)
            user.groups.add(group)
            return HttpResponseRedirect(reverse('login'))
    else:
        form = SignUpForm()
    return render(request, 'blogapp/signup.html', {'form' : form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged In Successfully")
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'blogapp/login.html', {'form':form})
    
    else:
        return HttpResponseRedirect('/dashboard/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                utitle = form.cleaned_data['title']
                udesc  = form.cleaned_data['desc']
                pst = Post(title=utitle, desc=udesc)
                pst.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            form = PostForm()
        return render(request, 'blogapp/addPost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')
    
    
def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi) 
        return render(request, 'blogapp/updatePost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')
    
def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')