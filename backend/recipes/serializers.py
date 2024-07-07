from rest_framework import serializers

from .models import *



class ListRecipeSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.category_name', allow_null=True)

    class Meta:
        model = Recipe
        fields = ['recipe_name', 'url_name', 'category']


class ListCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']





# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['category_name', 'category_icon']


# class IngredientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ingredient
#         fields = ['ingredient']


# class UnitSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Unit
#         fields = ['unit']


class IngredientToRecipeSerializer(serializers.ModelSerializer):
    ingredient = serializers.CharField(source='ingredient.ingredient_name')
    unit = serializers.CharField(source='unit.unit', allow_null=True)

    class Meta:
        model = IngredientToRecipe
        fields = ['ingredient', 'quantity', 'unit']


class RecipeSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    category = serializers.CharField(source='category.category_name', allow_null=True)
    ingredients = IngredientToRecipeSerializer(source='ingredient_amounts', many=True)

    class Meta:
        model = Recipe
        fields = ['recipe_name', 'category', 'description', 'recipe_picture', 'ingredients']