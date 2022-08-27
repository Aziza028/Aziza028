from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import User


class CustomUserAdmin(UserAdmin):
    model = User

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    readonly_fields = (
        "date_joined",
        "last_login",
    )

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "password",
                )
            },
        ),
        (
            ("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                )
            },
        ),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            ("Important dates"),
            {
                "fields": (
                    "date_joined",
                    "last_login",
                )
            },
        ),
        (
            ("Extra Info"),
            {
                "fields": (
                    "gender",
                    "blood_group",
                    "occupation",
                    "workplace",
                    "age",
                    "phone_number",
                    "present_address",
                    "permanent_address",
                    "last_blood_donation_date",
                ),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
