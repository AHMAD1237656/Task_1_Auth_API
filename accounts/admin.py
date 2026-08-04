from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Fields",
            {
                "fields": (
                    "role",
                    "is_email_verified",
                )
            },
        ),
    )

    list_display = (
        "username",
        "email",
        "role",
        "is_email_verified",
        "is_staff",
    )