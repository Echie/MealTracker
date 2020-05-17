from datetime import date, timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from meals.models import Meal, Recipe


def calculate_meal_score(meal_date):
    date_diff = (date.today() - meal_date).days
    return 1 if date_diff == 0 else max(1 - (date_diff / 30), 0)


def next_three_recipe_recommendations(meals):
    recipe_scores = {
        r_id: 0 for r_id in Recipe.objects.all().values_list("id", flat=True)
    }
    for meal in meals:
        recipe_scores[meal.recipe.id] += calculate_meal_score(meal.date)

    sorted_recipe_scores = sorted(recipe_scores.items(), key=lambda item: item[1])
    first_three_ids = [i[0] for i in sorted_recipe_scores[:3]]

    return Recipe.objects.filter(id__in=first_three_ids)


@login_required
def index(request):
    recent_meals = Meal.objects.filter(date__gte=date.today() - timedelta(days=30))
    context = {
        "meals": recent_meals,
        "recipes": Recipe.objects.all(),
        "recommendations": next_three_recipe_recommendations(recent_meals),
    }
    return render(request, "meals/index.html", context)
