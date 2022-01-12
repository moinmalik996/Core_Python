from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def fees_django(request):

    fees = {'charges' : '200 USD'}
    return render(request, 'fees/fees.html', context=fees)