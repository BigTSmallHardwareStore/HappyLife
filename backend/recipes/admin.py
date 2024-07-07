from django.contrib import admin
from .models import *
# Register your models here.


class IngredientInline(admin.TabularInline):
    model = IngredientToRecipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ("recipe_name", "category", "url_name")
    search_fields = ['recipe_name']
    inlines = [IngredientInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", )


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("ingredient_name", )
    search_fields = ['ingredient_name']
    ordering = ['ingredient_name']


class UnitAdmin(admin.ModelAdmin):
    list_display = ("unit", )


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Ingredient, IngredientAdmin)
