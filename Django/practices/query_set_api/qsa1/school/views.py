from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q

# Create your views here.


def home(request):
    # stu_data = Student.objects.all()
    # stu_data = Student.objects.filter(marks=700, city='Gujrat')
    # stu_data = Student.objects.exclude(marks=700)
    # stu_data = Student.objects.order_by('?') # Order by Random Data
    # stu_data = Student.objects.order_by('-marks') # Descending Order
    # stu_data = Student.objects.order_by('marks') # Ascending Order
    # stu_data = Student.objects.order_by('id').reverse()[:5]
    # stu_data = Student.objects.values('name', 'city') # Only Show the Specific Columns 
    # stu_data = Student.objects.values_list('id', flat=True)
    # stu_data = Student.objects.using('default')
    # stu_data = Student.objects.dates('pass_date', 'month')

    #-------------------Double Tale Start--------------------

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # stu_data = qs1.union(qs2)
    
    #---------Queries That Do Not Return QuerySets-----------
    
    # stu_data = Student.objects.get(pk=1)
    
    # stu_data = Student.objects.order_by('name').first()
    # stu_data = Student.objects.order_by('name').last()
    
    # stu_data = Student.objects.latest('pass_date')
    # stu_data = Student.objects.earliest('pass_date')
    
    stu_data = Student.objects.filter(Q(id=2) & Q(roll=10))
    

    print("Student Data")
    print("------------")
    print(stu_data.exists())
    print(stu_data)
    # print("SQL Query")
    # print("---------")
    # print(stu_data.query)
    return render(request, 'school/home.html', {'stu_data':stu_data})