from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render
from django.http import HttpResponseRedirect

# importing Forms Class
from .forms import StudentsRegistration


# Create your views here.
def thankyou(request):
    return render(request, 'enroll/success.html')

def show_form_data(request):

    if (request.method == "POST"):
        fm = StudentsRegistration(request.POST)
        if fm.is_valid():
            print("Form Validated")
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            print("Name     : ", name)
            print("Email    : ", email)
            print("Password : ", password)
            return HttpResponseRedirect('/student/success')
    else:
        print("Its coming from GET request.")
        fm = StudentsRegistration(auto_id="student_%s")

    return render(request, 'enroll/studentEnrollment.html', {'form': fm})
