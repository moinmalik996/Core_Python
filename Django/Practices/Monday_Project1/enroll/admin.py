from django.contrib import admin
from enroll.models import Student

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'stu_id', 'stu_name', 'stu_email', 'stu_pass')

# Register your models here.
admin.site.register(Student, StudentsAdmin)