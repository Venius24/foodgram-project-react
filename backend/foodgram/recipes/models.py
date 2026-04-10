from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    ingredients = models.TextField()
    time_to_cook = models.IntegerField()
    image = models.ImageField(upload_to='recipes/images/', blank=True, null=True)
    tag = models.ManyToManyField("Tag", related_name="recipes")
    ingredient = models.ManyToManyField("Ingredient")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=7, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    measurement_unit = models.CharField(max_length=200)

    def __str__(self):
        return self.name