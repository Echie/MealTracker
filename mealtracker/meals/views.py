from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from meals.models import Meal, Recipe


def next_three_recipe_recommendations(meals):
    eaten_recipe_ids = meals.values_list("recipe__id", flat=True)
    return Recipe.objects.exclude(id__in=eaten_recipe_ids)[:3]


@login_required
def index(request):
    recent_meals = Meal.objects.all()
    context = {
        "meals": recent_meals,
        "recipes": Recipe.objects.all(),
        "recommendations": next_three_recipe_recommendations(recent_meals),
    }
    return render(request, "meals/index.html", context)
