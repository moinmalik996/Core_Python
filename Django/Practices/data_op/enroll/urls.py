from django.urls import path
from . import views


urlpatterns = [
    path('all/', views.student_info),
    path('unique/', views.studnet_unique)
]