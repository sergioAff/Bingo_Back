from django.urls import path
from .views import get_user_count

urlpatterns = [
    path("get_user_count/", get_user_count, name="get_user_count"),  # API para obtener el número de usuarios
]
