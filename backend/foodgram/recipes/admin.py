from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Cart, Favorite, Ingredient, Recipe, Tag

@admin.register(Recipe)
class RecipeAdmin(ImportExportModelAdmin):
    list_display = ('name', 'author', 'favorite_counter')
    list_filter = ('name', 'author', 'tags')

    @admin.display(description='В избранном')
    def favorite_counter(self, obj):
        return obj.favorited.all().count()

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    list_filter = ('name',)

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
