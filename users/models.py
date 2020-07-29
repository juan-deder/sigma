from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    city = models.CharField(max_length=30)
    department = models.CharField(max_length=50)
