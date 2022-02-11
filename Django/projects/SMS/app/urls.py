from django.urls import path
from .views import (UserRegistration,
                    CustomLogin,
                    CustomLogoutView,
                    DashboardView,
                    
                    StudentView,
                    StudentCreate)


urlpatterns = [
    path('dashboard/', DashboardView.as_view() ,name='dashboard'),
    path('signup/', UserRegistration.as_view(), name='signup'),
    path('login/', CustomLogin.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    
    path('students/', StudentView.as_view(), name='studentlist'),
    path('students/create/', StudentCreate.as_view(), name='studentcreate')
]