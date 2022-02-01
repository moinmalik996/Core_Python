from django.shortcuts import render, HttpResponse

from .models import Student
from .serializers import StudentSerializer

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

import io
import json
# Create your views here.


def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        # stream = io.BytesIO(json_data)
        # print("")
        # print(json_data)
        # print("")
        # print(stream)
        
        pythondata = JSONParser().parse(request.body)
        
        id = pythondata.get('id', None)
        if id is not None:
            stu = Student.objects.get(id= id)
            stu_ser = StudentSerializer(stu)
            json_data = JSONRenderer().render(stu_ser.data)
            return HttpResponse(json_data, content_type='application/json')
    
    stu = Student.objects.all()
    stu_ser = StudentSerializer(stu, many=True)
    json_data = JSONRenderer().render(stu_ser.data)
    return HttpResponse(json_data, content_type='application/json')
        