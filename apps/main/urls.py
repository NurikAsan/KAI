from django.urls import path
from .views.main import MainListAPIView
from .views.news import NewsRetrieveAPIView
from .views.advirtisements import AdvertisementsRetrieveView


urlpatterns = [
    path('main/', MainListAPIView.as_view()),
    path('news/<int:pk>/', NewsRetrieveAPIView.as_view()),
    path('advertisement/<int:pk>/', AdvertisementsRetrieveView.as_view()),
]
