from django.contrib import admin

# importar as models
from .models import Category, Recipe


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...


#admin.site.register(Category, CategoryAdmin)

