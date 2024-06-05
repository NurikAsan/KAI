from django.urls import path
from .views import page_generator
from .views.category import CategoriesListView


urlpatterns = [
    path('page-generator/<int:cat_id>/<int:sub_cat_id>/',
         page_generator.PageGeneratorRetrieveView.as_view()),
    path('page-generator/<int:cat_id>/<int:sub_cat_id>/<int:sub_sub_cat_id>/',
         page_generator.PageGeneratorRetrieveView.as_view()),
    path('categories/', CategoriesListView.as_view())
]
