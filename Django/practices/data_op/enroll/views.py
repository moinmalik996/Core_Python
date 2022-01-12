from django.shortcuts import render

# Importing Models
from enroll.models import Student

# Create your views here.

def student_info(request,*args,**kwargs):
    
    stu_db_data = Student.objects.all()
    print(stu_db_data)
    my_data = {'stu_data' : stu_db_data}

    return render(request, 'enroll/all.html', my_data)

def studnet_unique(request):

    stu_db_data = Student.objects.get(pk=1)
    print("My OutPut :  ", stu_db_data)
    my_data = {'stu_data' : stu_db_data}

    return render(request, 'enroll/unique.html', my_data)
