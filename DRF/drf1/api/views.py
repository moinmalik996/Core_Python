from django.shortcuts import render, HttpResponse
from .models import Student
from .serializers import StudentSerializer

from rest_framework.renderers import JSONRenderer


# Create your views here.


def student_details(request, pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    print(serializer)
    json_data = JSONRenderer().render(serializer.data)
    print(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    print(serializer)
    json_data = JSONRenderer().render(serializer.data)  # It is a list of JSON Data
    print(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
