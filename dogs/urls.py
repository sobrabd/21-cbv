from django.urls import path
from .apps import DogsConfig
from . import views

app_name = DogsConfig.name

urlpatterns = [
    path("", views.index, name="index"),
    path("categories/", views.categories, name="categories"),
    path('<int:pk>/dogs', views.category_dogs, name='category_dogs')
]
