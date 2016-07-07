from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    token = models.CharField(max_length=200)
