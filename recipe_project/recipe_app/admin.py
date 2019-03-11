from django.contrib import admin
from .models import RecipeModel, UserModel

# Models for users and recipes
admin.site.register(RecipeModel)
admin.site.register(UserModel)
