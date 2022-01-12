from django.contrib import admin

# Register your models here.

from .models import StudentData

@admin.register(StudentData)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'pass_w']