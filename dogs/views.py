from django.shortcuts import render
from .models import Category, Dog


# Create your views here.
def index(request):
    context = {
        'objects_list': Category.objects.all()[:3],
        'title': 'Питомник - Добро пожаловать'
    }

    return render(request, 'dogs/index.html', context)


def categories(request):
    context = {
        'objects_list': Category.objects.all(),
        'title': 'Питомник - Наши породы'
    }

    return render(request, 'dogs/categories.html', context)


def category_dogs(request, pk):
    category = Category.objects.get(pk=pk)
    context = {
        'objects_list': Dog.objects.filter(category_id=pk),
        'title': f'Все собаки породы {category.name}'
    }

    return render(request, 'dogs/dogs.html', context)