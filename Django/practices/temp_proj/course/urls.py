from django.urls import path
from . import views

urlpatterns = [
    path('learndj/', views.learn_django),
    path('awesome/', views.my_filters),
    path('ifcondition', views.if_conditions)
]