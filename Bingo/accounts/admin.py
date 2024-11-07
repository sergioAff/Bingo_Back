from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

class UserAdmin(BaseUserAdmin):
    ordering=['email']
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=User
    list_display=['email','first_name','last_name','is_active','is_staff']
    list_display_links = ['email']
    list_filter = ['email', 'first_name', 'last_name', 'is_active', 'is_staff']
    search_fields = ['email', 'first_name', 'last_name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', "first_name","last_name",'password1', 'password2', 'first_name', 'last_name', 'is_active', 'is_staff')}
        ),
    )

admin.site.register(User, UserAdmin)

