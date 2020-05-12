from django.shortcuts import render
from rest_framework import generics
from blogs.models import Post
from .serializers import PostSerializer

class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
