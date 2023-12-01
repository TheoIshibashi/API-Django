from django.contrib import admin
from app.domains.users.models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "role",
    ]


admin.site.register(User, UserAdmin)
