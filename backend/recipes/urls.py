from django.urls import path

from . import api

urlpatterns = [
    path('', api.all_recipes, name='all_recipes'),
    path('<str:url_name>', api.show_recipe, name='single_recipe')
]