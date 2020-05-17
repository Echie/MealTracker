from datetime import date

from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField("Ingredient")

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    amount = models.CharField(max_length=255, blank=True, default="")

    def __str__(self):
        amount = f": {self.amount}" if self.amount else ""
        return f"{self.name}{amount}"


class Meal(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.date}: {self.recipe.name}"
