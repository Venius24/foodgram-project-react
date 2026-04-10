from rest_framework import serializers
from .models import Recipe, Tag, Ingredient
from users.serializers import CustomUserSerializer # Или твой сериализатор пользователя

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'slug')

class IngredientSerializer(serializers.ModelSerializer):
    # Тут важно: это для списка ингредиентов в рецепте с количеством
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'measurement_unit')

class RecipeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='title')
    author = CustomUserSerializer(read_only=True)
    tag = TagSerializer(many=True, read_only=True)
    cooking_time = serializers.IntegerField(source='time_to_cook')
    text = serializers.CharField(source='description')
    ingredients = IngredientSerializer(many=True, read_only=True, source='ingredient')
    
    class Meta:
        model = Recipe
        fields = ('id', 'tag', 'author', 'name', 'image', 'text', 'cooking_time', 'ingredients')