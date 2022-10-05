from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('id', 'email', 'is_superuser', 'is_active')
    search_fields = ('id', 'email', 'first_name', 'last_name')
    list_filter = ('is_superuser', 'is_active')

    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2'),
            },
        ),
    )

    fieldsets = (
        (
            _('Login data'), {
                'fields': ('email', 'password'),
            },
        ),
        (
            _('Personal info'), {
                'fields': ('first_name', 'last_name'),
            },
        ),
        (
            _('Permissions'), {
                'fields': ('is_active', 'is_superuser'),
            },
        ),
    )

    ordering = ('email',)
