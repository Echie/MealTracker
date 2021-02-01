from django.contrib import admin

from .models import Ingredient, Meal, Recipe


class IngredientInlineAdmin(admin.TabularInline):
    model = Recipe.ingredients.through


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = ["name"]
    inlines = [IngredientInlineAdmin]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    pass
