from django.urls import path

from .views import (Tasklist, 
                    TaskDetail, 
                    TaskCreate, 
                    TaskUpdate,
                    TaskDelete,
                    
                    CustomLoginView,
                    CustomLogoutView,
                    RegisterPage)


urlpatterns = [
    path('register/', RegisterPage.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    
    path('', Tasklist.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('create_task/', TaskCreate.as_view(), name='task_create'),
    path('update_task/<int:pk>', TaskUpdate.as_view(), name='task_update'),
    path('delete_task/<int:pk>', TaskDelete.as_view(), name='task_delete')
]