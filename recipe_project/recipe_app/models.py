from django.db import models
from datetime import date
from django.contrib.auth.models import User


# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=500, default='')
    password = models.CharField(max_length=500, default='')
    email = models.EmailField(default='')
    fk_to_User = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class RecipeModel(models.Model):
    image = models.CharField(max_length=1000, default='')
    name = models.CharField(max_length=500, default='')
    description = models.TextField(default='')
    date_create = models.DateField(default=date.today)
    creator = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
