from django.shortcuts import render, HttpResponse
from django.views import View
from .forms import ContactForm

# Create your views here.


# class MyView(View):
#     name = 'Moin Malik'
#     def get(self, request):
        
#         # return HttpResponse("<h1>My Class Based View - GET </h1>")
#         context = {'msg':'This is Class Based View with template'}
#         return render(request, 'app/home.html', context)


class ContactView(View):
    
    def get(self, request):
        form = ContactForm()
        return render(request, 'app/home.html', {'form':form})
    
    def post(self, request):
        form = ContactForm()
        if form.is_valid():
            print(form.cleaned_data['name'])
        return HttpResponse("Your Data is Submitted")
        
