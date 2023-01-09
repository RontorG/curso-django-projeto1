from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from utils.recipes.factory import makeRecipe
from .models import Recipe

# Create your views here.
def home(request):
    recipes = Recipe.objects.filter(
            is_published=True
            ).order_by('-id')

    return render(request, 'recipes/pages/home.html', context={
    'recipes' : recipes,
    })


def category(request, category_id):
    recipes = get_list_or_404(
            Recipe.objects.filter(
                category__id=category_id,
                is_published=True
            ).order_by('-id'))
            
    return render(request, 'recipes/pages/category.html', context={
        'recipes' : recipes,
        'category' : f'{recipes[0].category.name.capitalize()} - Category',
    })


def recipe(request, id):
    recipe = Recipe.objects.filter(
                pk=id,
                is_published=True
            ).order_by('-id').first()

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe' : recipe,
        'is_detail_page' : True,
    })

