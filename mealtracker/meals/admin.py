from django.contrib import admin

from mealtracker.gkeep.main import add_shopping_list_item

from .models import Ingredient, Meal, Recipe


class IngredientInlineAdmin(admin.TabularInline):
    model = Recipe.ingredients.through


def add_to_shopping_list(modeladmin, request, queryset):
    add_shopping_list_item()


add_to_shopping_list.short_description = "Add recipe to Google Keep"


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = ["name"]
    inlines = [IngredientInlineAdmin]
    actions = [add_to_shopping_list]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    pass
