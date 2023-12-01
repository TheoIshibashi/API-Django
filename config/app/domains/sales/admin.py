from django.contrib import admin
from app.domains.sales.models import Sales

# Register your models here.


class SalesAdmin(admin.ModelAdmin):
    list_display = [
        "value",
        "amount",
        "product",
        "description",
        "created_at",
        "updated_at",
    ]


admin.site.register(Sales, SalesAdmin)
