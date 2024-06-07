from django.urls import path
from .views.news import NewsRetrieveAPIView, NewsListAPIView
from .views.advirtisements import AdvertisementsRetrieveView, AdvertisementsListView


urlpatterns = [
    path('news/', NewsListAPIView.as_view()),
    path('news/<int:pk>/', NewsRetrieveAPIView.as_view()),
    path('advertisement/', AdvertisementsListView.as_view()),
    path('advertisement/<int:pk>/', AdvertisementsRetrieveView.as_view()),
]
