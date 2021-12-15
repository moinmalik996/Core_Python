from django.urls import path
from django.urls import path
from . import views              # dot is for current directory

urlpatterns = [
    path('learndj/', views.learn_django),
    path('learnpython/', views.learn_python)
]