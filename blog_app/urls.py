from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('edit_blog/', views.edit_blog, name='edit_blog'),
    path('delete_blog/', views.delete_blog, name='delete_blog'),
    path('reply_blog/', views.reply_blog, name='reply_blog'),
    path('query_blog_by_priority/', views.query_blog_by_priority, name='query_blog_by_priority'),
    path('search_blog/', views.search_blog, name='search_blog'),
]
