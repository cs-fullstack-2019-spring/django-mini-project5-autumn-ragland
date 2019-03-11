from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new_user', views.new_user, name='new_user'),
    path('edit_user', views.edit_user, name='edit_user'),
    path('all_recipes', views.all_recipes, name='all_recipes'),
    path('new_recipe', views.new_recipe, name='new_recipe'),
    path('profile', views.profile, name='profile'),
]
