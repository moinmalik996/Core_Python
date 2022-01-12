from django.urls import path
from . import views


urlpatterns = [
    path('registration/', views.show_form_data),
    path('success/', views.thankyou)
]