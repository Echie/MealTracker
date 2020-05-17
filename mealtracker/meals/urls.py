from django.urls import path
from meals.views import index

urlpatterns = [
    path("", index, name="index"),
]
