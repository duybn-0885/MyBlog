from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import generics

from blogs.models import Post
from .serializers import PostSerializer, UserSerializer
from blogs.permissions import IsReadOnly

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsReadOnly,)
