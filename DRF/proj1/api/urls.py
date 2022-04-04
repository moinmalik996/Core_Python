from django.urls import path
from .views import PostList, PostDetail


app_name = 'blog_api'

urlpatterns = [
    path('post/<int:pk>', PostDetail.as_view(), name='detailpost'),
    path('', PostList.as_view(), name='listpost')
]