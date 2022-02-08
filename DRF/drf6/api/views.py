
# Generic API View and ModelMixin

from .models import Student
from .serializers import StudentSerializer

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (ListModelMixin, 
                                   CreateModelMixin,
                                   UpdateModelMixin,
                                   DestroyModelMixin,
                                   RetrieveModelMixin)


# List & Create - PK is not required
class Stu_List_Create_API(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
# Update , Delete, Retrieve - PK is Required
class Stu_Up_Del_Ret_API(GenericAPIView, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    