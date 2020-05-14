from django.urls import path
from .views import PostDetail, PostList, UserList, UserDetail

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
]
