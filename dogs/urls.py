from django.urls import path
from .apps import DogsConfig
from . import views

app_name = DogsConfig.name

urlpatterns = [
    path("", views.index, name="index"),
    path("categories/", views.CategoryListView.as_view(), name="categories"),
    path('<int:pk>/dogs', views.DogListView.as_view(), name='category_dogs')
]
