from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class AppUser(AbstractUser):
    pass


class Note(models.Model):
    author = models.ForeignKey(AppUser, related_name='notes', on_delete=models.CASCADE)
    text = models.TextField()
