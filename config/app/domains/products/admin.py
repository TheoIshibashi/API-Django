from django.contrib import admin
from app.domains.products.models import Product

# Register your models here.


class ProductsAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "value",
        "category",
        "description",
        "created_at",
        "updated_at",
    ]


admin.site.register(Product, ProductsAdmin)
