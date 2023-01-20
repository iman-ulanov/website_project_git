from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return self.username


class Author(models.Model):
    is_author = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


