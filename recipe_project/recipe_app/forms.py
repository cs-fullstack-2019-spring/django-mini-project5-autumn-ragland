from django import forms
from .models import UserModel, RecipeModel


# new user/edit user info
class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        exclude = ['fk_to_User']


# new recipe
class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeModel
        exclude = ['creator']
