from django.shortcuts import render

from .models import Student
from .serializers import StudentSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

class StudentModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
      