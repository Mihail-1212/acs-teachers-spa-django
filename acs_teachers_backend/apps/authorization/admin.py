from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import AuthUserCreationForm, AuthUserChangeForm


class AuthUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('last_name', 'first_name', 'second_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    model = User

    add_form = AuthUserCreationForm
    form = AuthUserChangeForm
    
    list_display = ['username', 'email', 'last_name', 'first_name', 'second_name', 'is_staff']

admin.site.register(User, AuthUserAdmin)
