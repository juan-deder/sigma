import re

from django.core.exceptions import ValidationError
from django.db import models


def email_validator(email):
    if not re.search('.+@.+', email):
        raise ValidationError(f'{email} is not a valid email.')


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30, validators=[email_validator])
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=50)
