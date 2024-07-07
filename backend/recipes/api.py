from django.conf import settings

from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import *

from .serializers import *


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def all_recipes(request):
    all_recipes = Recipe.objects.all()
    all_categories = Category.objects.all()

    recipe_serializer = ListRecipeSerializer(all_recipes, many=True)
    category_serializer = ListCategorySerializer(all_categories, many=True)


    return JsonResponse({
            'categories': category_serializer.data,
            'recipes': recipe_serializer.data,
        }, safe=False)




@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def show_recipe(request, url_name):
    recipe = Recipe.objects.filter(url_name=url_name)[0]

    serializers = RecipeSerializer(recipe)

    return JsonResponse(serializers.data, safe=False)

    

