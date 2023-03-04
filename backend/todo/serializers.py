
# import serializers from the REST framework
from rest_framework import serializers
 
# import the todo data model
from .models import Recipe
from .models import Ingredient
from .models import User
 
# create a serializer class
class RecipeSerializer(serializers.ModelSerializer):
 
    # create a meta class
    class Meta:
        model = Recipe
        fields = ('id', 'title','ingredients','expScore')

class UserSerializer(serializers.ModelSerializer):
 
    # create a meta class
    class Meta:
        model = User
        fields = ('id', 'name', 'recipes')

class IngredientSerializer(serializers.ModelSerializer):
 
    # create a meta class
    class Meta:
        model = Ingredient
        fields = ('id', 'title', 'expDate')