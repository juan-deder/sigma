from django.db import models


class User(models.Model):
    name = models.CharField(max_length=99)
    email = models.EmailField(max_length=99)
    city = models.CharField(max_length=99)
    department = models.CharField(max_length=99)
