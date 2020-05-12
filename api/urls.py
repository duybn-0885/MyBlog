from django.urls import path
from .views import PostAPIView

urlpatterns = [
    path('', PostAPIView.as_view()),
]
