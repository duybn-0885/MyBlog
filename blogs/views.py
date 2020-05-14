from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsReadOnly
from rest_framework import generics, permissions, viewsets
from django.contrib.auth import get_user_model

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
