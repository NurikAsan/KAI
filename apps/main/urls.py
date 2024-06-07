from django.urls import path
from .views.main import MainListAPIView


urlpatterns = [
    path('main/', MainListAPIView.as_view()),
]
