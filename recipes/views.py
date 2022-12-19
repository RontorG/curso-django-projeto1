from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import makeRecipe

# Create your views here.
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes' : [makeRecipe() for _ in range(10)],
        })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe' : makeRecipe(),
        })

