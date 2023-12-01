from django.db import models
from app.domains.products.models import Product


class Sales(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    value = models.FloatField()
    amount = models.IntegerField()
    description = models.CharField(max_length=258, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
