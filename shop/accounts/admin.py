from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, ProfileUser, Address, OtpCode


class ProfileInline(admin.StackedInline):
    model = ProfileUser
    can_delete = False
    extra: int = 0


class AddressInline(admin.StackedInline):
    model = Address
    extra = 1


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
    search_fields = ('email','phone')
    ordering = ('date_joined',)
    date_hierarchy= 'date_joined'

    inlines = (ProfileInline, AddressInline)


@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ('phone', 'code', 'created_at')


