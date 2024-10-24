# posts/urls.py
from django.urls import path
from .views import PostBlogPost, GetUpdateDeletePost

urlpatterns = [
    path('posts/', PostBlogPost.as_view(), name='post'),
    path('posts/<int:pk>/', GetUpdateDeletePost.as_view(), name='get_put_delete'),
]
