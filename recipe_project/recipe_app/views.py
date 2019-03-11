from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserModel, UserForm, RecipeModel, RecipeForm
from django.http import HttpResponse
from django.contrib.auth.models import User


# index/home page
def index(request):
    # get all recipes created by the logged in user
    if request.user.is_authenticated:
        current_user = UserModel.objects.get(name=request.user)
        my_recipes = RecipeModel.objects.filter(creator=current_user)
    # if the user is not logged in don's show any recipes
    else:
        my_recipes = ''
    # pass the recipes to the page
    context = {
        'my_recipes': my_recipes
    }
    return render(request, 'recipe_app/index.html', context)


# create a new user
def new_user(request):
    form = UserForm(request.POST or None)
    if request.method == 'POST':
        # save to django user table
        User.objects.create_user(request.POST["name"], "", request.POST["password"])
        # save form
        form.save()
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'recipe_app/new_user.html', context)


# edit user info BROKEN
def edit_user(request):
    # user_item = get_object_or_404(UserModel, pk=request.user)
    # user_form = UserForm(request.POST or None, instance=user_item)
    # context = {
    #     'form': user_form
    # }
    # if request.method == 'POST':
    #     user_form.save()
    #     return redirect('home')
    # return render(request, 'recipe_app/new_user.html', context)
    return HttpResponse('not working')


# all recipes created by all users
def all_recipes(request):
    # get all recipes
    recipes = RecipeModel.objects.all()
    # pass all recipes to the page
    context = {
        'recipes': recipes
    }
    return render(request, 'recipe_app/all_recipes.html', context)


# show recipe details
def recipe_details(request, ID):
    # get recipe by id
    recipe_item = get_object_or_404(RecipeModel, pk=ID)

    # render recipe info
    context = {
        'recipe': recipe_item
    }

    return render(request, 'recipe_app/recipe_details.html', context)


# edit recipe info
def edit_recipe(request, ID):
    # get recipe by id
    recipe_item = get_object_or_404(RecipeModel, pk=ID)
    recipe_form = RecipeForm(request.POST or None, instance=recipe_item)

    # render populated form
    context = {
        'form': recipe_form
    }

    # save edited form
    if request.method == 'POST':
        recipe_form.save()
        return redirect('home')

    return render(request, 'recipe_app/new_recipe.html', context)


# create a new recipe
def new_recipe(request):
    form = RecipeForm(request.POST or None)
    # load recipe form
    context = {
        'form': form
    }
    if request.method == 'POST':
        current_user = UserModel.objects.get(name=request.user)
        # add recipe to model with fk of logged in user
        RecipeModel.objects.create(name=request.POST['name'], image=request.POST['image'],
                                   description=request.POST['description'],
                                   date_create=request.POST['date_create'],
                                   creator=current_user)
        return redirect('home')
    return render(request, 'recipe_app/new_recipe.html', context)
