from django.db import models
from django.contrib import auth
# Create your models here.

class User(auth.models.User, auth.models.PermissionsMixin):
    """This class is inherited from base User class and the permissions mixin"""

    def __str__(self):
        return f"@{self.username}" #This username come from the inherited class
