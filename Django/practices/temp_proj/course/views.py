from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def learn_django(request):

    course_details = {'c_name' : 'Django',
                      'c_duration' : '8 Months',
                      'c_seats' : '8'}

    return render(request, 'courses/course.html', context=course_details)


def my_filters(request):

    title = "Django is Awesome"

    my_dict = {'title' : title}

    return render(request, 'courses/awesome.html', my_dict)


def if_conditions(request):

    myname = 'Moin Malik'

    data = {'myname' : myname}

    return render(request, 'courses/ifcondition.html', data)
