from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy

# Classes for Authentication Functionality and User Creation
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Classes for Authorization and Permision
from django.contrib.auth.mixins import LoginRequiredMixin

# Classes for Defining Views
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, 
                                       UpdateView, 
                                       DeleteView,
                                       FormView)

from .models import Student, Teacher
# Create your views here.


class UserRegistration(FormView):
    template_name = 'app/signup.html'
    form_class    = UserCreationForm
    redirect_authenticated_user = True
    success_url   = reverse_lazy('login')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserRegistration, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('')
        return super(UserRegistration, self).get(*args, **kwargs)
    
    
    
class CustomLogin(LoginView):
    template_name = 'app/login.html'
    fields        = "__all__"
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('dashboard')
    
    
class CustomLogoutView(LogoutView):
    next_page = 'login'
       
   
class DashboardView(LoginRequiredMixin, ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'app/dashboard.html'
    
    
class StudentView(LoginRequiredMixin, ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'app/student_list.html'
    
    
class StudentCreate(LoginRequiredMixin, CreateView):
    model = Student
    fields = '__all__'
    template_name = 'app/student_create.html'
    success_url = '/students'
    

  
    
    
    
    