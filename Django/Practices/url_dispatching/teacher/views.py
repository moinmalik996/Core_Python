from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def teacher_name(request):
    return HttpResponse("<h1>Sir Moin Abbas</h1>")

def teacher_age(request):
    return HttpResponse("<h1>23</h1>")