from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=258, blank=False)
    category = models.CharField(max_length=258, blank=False)
    value = models.FloatField()
    description = models.CharField(max_length=258, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
