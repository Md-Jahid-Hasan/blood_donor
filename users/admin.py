from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from users import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'first_name']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name',
                                         'date_of_birth',)}),
        (_('Permission'), {'fields': ('is_active', 'is_superuser')}),
        (_('Important Dates'), {'fields': ('date_joined', 'last_login')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        })
    )


admin.site.register(models.User, UserAdmin)

