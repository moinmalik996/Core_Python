from django.urls import path
from . import views

urlpatterns = [
    path("teacherName/", views.teacher_name),
    path("teacherAge/", views.teacher_age)
]