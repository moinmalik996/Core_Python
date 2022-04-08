from django.contrib import admin
from .models import Page
# Register your models here.

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'p_cat', 'p_date', 'user']