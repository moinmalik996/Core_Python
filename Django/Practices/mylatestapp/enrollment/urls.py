from django.urls import path

#importing app views
from . import views

urlpatterns = [
    path('dataupload/', views.collect_data_func),
    path('thankyou/', views.thankyou)
]