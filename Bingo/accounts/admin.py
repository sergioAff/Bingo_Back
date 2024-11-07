from django.contrib import admin
from . import models
from django.contrib.auth import get_user_model
User=get_user_model()

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active',"is_superuser")
    list_display_links = ('email','first_name', 'last_name')
    search_fields = ('email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser')
    list_per_page=25
    list_filter = ('is_staff', 'is_active')
    ordering = ('email', 'first_name', 'last_name')
    
admin.site.register(User, UserAdmin)
