from django.shortcuts import render
from .forms import UserModel, UserForm, RecipeModel, RecipeForm
from django.contrib.auth.models import User


# index/home page
def index(request):
    my_recipes = RecipeModel.objects.all
    context = {
        'my_recipes': my_recipes
    }
    return render(request, 'recipe_app/index.html', context)


# create a new user
def new_user(request):
    form = UserForm(request.POST or None)
    context = {
        'form': form
    }
    return render(request, 'recipe_app/new_user.html', context)


# edit user info
def edit_user(request):
    form = UserForm(request.POST or None)
    context = {
        'form': form
    }
    return render(request, 'recipe_app/new_user.html', context)


# all recipes created by all users
def all_recipes(request):
    recipes = RecipeModel.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'recipe_app/all_recipes.html', context)


# create a new recipe
def new_recipe(request):
    form = RecipeForm(request.POST or None)
    context = {
        'form': form
    }
    return render(request, 'recipe_app/new_recipe.html', context)


# view and edit profile
def profile(request):
    form = UserForm(request.POST or None)
    context = {
        'form': form
    }
    return render(request, 'recipe_app/profile.html', context)
