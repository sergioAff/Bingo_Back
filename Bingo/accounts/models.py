from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(_("Email Address"),unique=True, max_length=100)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True, blank=True, null=True)
    
    # Campos adicionales
    first_name = models.CharField(_("First Name"),max_length=100)
    last_name = models.CharField(_("Last Name"),max_length=100)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    objects = CustomUserManager()
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.email
    
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        