from django.db import models

# Create your models here.

class Ingredient(models.Model):
    title=models.CharField(max_length=150)
    expDate=models.CharField(max_length=150)

class Recipe(models.Model):
    title=models.CharField(max_length=150)
    ingredients=models.ListField(child=Ingredient, allow_empty=True, min_length=None, max_length=None)
    expScore=models.FloatField(max_value=None, min_value=None)


class User(models.Model):
    title=models.CharField(max_length=150)
    recipes=models.ListField(child=Recipe, allow_empty=True, min_length=None, max_length=None)

    # string representation of class
    def __str__(self):
        return self.title
