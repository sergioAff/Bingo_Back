from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email','password', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']