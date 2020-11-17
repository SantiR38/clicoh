"""Product models."""

# Django
from django.db import models

class Product(models.Model):
    """Product model."""

    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=25)
    price = models.FloatField()