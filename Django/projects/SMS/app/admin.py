from django.contrib import admin

# Register your models here.
from .models import Student, Teacher

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'fathername', 'roll', 'section', 'standard', 'city']
    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'subject', 'salary', 'city']