# posts/views.py
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# POST a blog post
class PostBlogPost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Get, Update, Delete a specific post
class GetUpdateDeletePost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
