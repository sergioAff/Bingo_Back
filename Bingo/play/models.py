# models.py
from django.db import models
from accounts.models import User

class Room(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Room Name")
    player_count = models.IntegerField(default=0, verbose_name="Players Count")  # Nuevo campo para el conteo

    def __str__(self):
        return self.name
