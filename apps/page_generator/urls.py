from .views import *
from django.urls import path
from .views import page_generator


# urlpatterns = [
#     path('nav_links/', NavView.as_view()),
#     path('nav_links/<str:pk>/', NavView.as_view()),
#     path('text_content/', TextContentView.as_view()),
#     path('text-content/<str:pk>/', TextContentView.as_view()),
#     path('veteran/', VeteranView.as_view()),
#     path('veteran/<str:pk>/', VeteranView.as_view()),
#     path('partner/', PartnersView.as_view()),
#     path('partner/<str:pk>/', PartnersView.as_view()),
#     path('news/', NewsView.as_view()),
#     path('news/<str:pk>/', NewsView.as_view()),
# ]

urlpatterns = [
    path('', page_generator.PageGeneratorListView.as_view())
]
