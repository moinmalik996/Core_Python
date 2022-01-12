"""LoginCount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from blogapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view),
    path('aboutus/', views.about_view, name='aboutus'),
    path('contactus/', views.contact_view, name='contactus'),
    path('dashboard/', views.dash_view, name='dashboard'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('addpost/', views.add_post, name='addPost'),
    path('update/post_<int:id>/edit', views.update_post, name='updatePost'),
    path('delete/post_<int:id>/delete', views.delete_post, name='deletePost')
]
