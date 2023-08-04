from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, Dog


# Create your views here.
def index(request):
    context = {
        'objects_list': Category.objects.all()[:3],
        'title': 'Питомник - Добро пожаловать'
    }

    return render(request, 'dogs/index.html', context)



class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Питомник - Наши породы'
    }


class DogListView(ListView):
    model = Dog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset
    
    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['object_list'] = Dog.objects.filter(category_id=category_item.pk)
        context_data['title'] = f'Все собаки породы {category_item.name}'

        return context_data


# def category_dogs(request, pk):
#     category = Category.objects.get(pk=pk)
#     context = {
#         'objects_list': Dog.objects.filter(category_id=pk),
#         'title': f'Все собаки породы {category.name}'
#     }

#     return render(request, 'dogs/dogs.html', context)

# def categories(request):
#     context = {
#         'objects_list': Category.objects.all(),
#         'title': 'Питомник - Наши породы'
#     }

#     return render(request, 'dogs/categories.html', context)