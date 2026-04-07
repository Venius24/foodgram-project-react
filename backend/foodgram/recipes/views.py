from rest_framework import viewsets
from .models import Recipe, Tag, Ingredient
from .serializers import RecipeSerializer, TagSerializer, IngredientSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def list(self, request, *args, **kwargs):
        from django.db import connection
        print(f"DEBUG: Подключен к БД: {connection.settings_dict['NAME']}")
        print(f"DEBUG: Хост: {connection.settings_dict['HOST']}")
        print(f"DEBUG: Объектов в базе: {Tag.objects.count()}")
        return super().list(request, *args, **kwargs)

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
