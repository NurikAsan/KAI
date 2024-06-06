from django.urls import path
from .views.main import MainListAPIView
from .views.news import NewsRetrieveAPIView


urlpatterns = [
    path('main/', MainListAPIView.as_view()),
    path('news/<int:pk>/', NewsRetrieveAPIView.as_view()),
]
