from django.shortcuts import render
from .models import Student


# Create your views here.


def home(request):
    stu_data = Student.objects.all()
    context = {'stu_data':stu_data}
    print("Student Data")
    print("------------")
    print(context)
    print("SQL Query")
    print("---------")
    print(stu_data.query)
    return render(request, 'school/home.html', context)