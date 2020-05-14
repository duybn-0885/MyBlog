from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from .permissions import IsReadOnly
from rest_framework import generics, permissions

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsReadOnly,)
