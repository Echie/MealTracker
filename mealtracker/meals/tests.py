from datetime import date, timedelta

from django.test import TestCase
from meals.models import Meal, Recipe
from meals.views import next_three_recipe_recommendations


class MealTestCase(TestCase):
    def setUp(self):
        for i in range(1, 6):
            Recipe.objects.create(name=f"recipe {i}")
        self.eaten_recipe = Recipe.objects.get(name="recipe 1")
        Meal.objects.create(
            recipe=self.eaten_recipe, date=date.today() - timedelta(days=1)
        )

    def test_recipes(self):
        meals = Meal.objects.all()
        recommendations = next_three_recipe_recommendations(meals)
        self.assertTrue(self.eaten_recipe not in recommendations)
        self.assertTrue(len(recommendations), 3)
