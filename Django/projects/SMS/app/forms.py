from django import forms

from .models import Student, Teacher


class StudentForm(forms.ModelForm):
    class Meta:
        
        model = Student
        
        
class TeacherForm(forms.ModelForm):
    class Meta:
        
        model = Teacher
        

        