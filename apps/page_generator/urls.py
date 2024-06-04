from django.urls import path
from .views import page_generator

urlpatterns = [
    path('', page_generator.PageGeneratorListView.as_view())
]