from django.urls import path
from . import views

urlpatterns = [
    # home page/login/new user/my recipes
    path('', views.index, name='home'),
    # create a new user
    path('new_user/', views.new_user, name='new_user'),
    # view all recipes by all users
    path('all_recipes/', views.all_recipes, name='all_recipes'),
    # edit user recipes
    path('edit_recipe/<int:ID>', views.edit_recipe, name='edit_recipe'),
    # create a new recipe
    path('new_recipe/', views.new_recipe, name='new_recipe'),
    # details of recipes
    path('recipe_details/<int:ID>', views.recipe_details, name='recipe_details'),
    # view user profile
    path('profile/', views.profile, name='profile'),
    # edit user profile information
    path('edit_user/<int:ID>', views.edit_user, name='edit_user'),
]
