from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>Home</h1>")


def learn_django(request):
    return HttpResponse("<h1>Hello Django</h1>")

def learn_python(request):
    return HttpResponse("<h1>Learn Python</h1>")

def learn_var(request):
    a = 10 + 10
    return HttpResponse("<h1>{a}</h1>")

def learn_format(request):
    name = "Moin Malik"
    return HttpResponse(f"<h1>My name is {name}.</h1>")