from django import forms
from .models import UserModel, RecipeModel


# new user
class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        exclude = ['fk_to_User']


# edit user info
class EditUserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['name', 'email', 'image']


# new recipe
class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeModel
        exclude = ['creator']
