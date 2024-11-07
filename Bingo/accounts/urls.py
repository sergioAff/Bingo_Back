from django.urls import path, re_path
from . import views

urlpatterns = [
    path('register/', views.register , name='register'),
    path('login/', views.login, name='login'),
    path('user/', views.user_profile, name='user-detail'),
    re_path('login', views.login, name='login'),
    re_path('register', views.register, name='register'),
    re_path('logout', views.logout, name='logout'),
    re_path('user', views.user_profile, name='user-detail'),
]
