from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, ProfileUser, Address, OtpCode


class ProfileInline(admin.StackedInline):
    model = ProfileUser
    can_delete = False


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('phone', 'email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {"fields": ("phone", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
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
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone", "password1", "password2"),
            },
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

    inlines = (ProfileInline,)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    pass
