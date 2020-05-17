from django.shortcuts import render

from rest_framework import generics

from blogs.models import Post
from blogs.permissions import IsReadOnly
from .serializers import PostSerializer

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsReadOnly,)
