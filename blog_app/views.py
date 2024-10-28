# posts/views.py
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostBlogPost(generics.CreateAPIView):
    """Create a new post."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class GetUpdateDeletePost(generics.RetrieveUpdateDestroyAPIView):
    """Get, update or delete a post."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class GetAllPosts(generics.ListAPIView):
    """Get all posts."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
