from django.urls import path, include
from . import views

urlpatterns = [
    path('register/',views.register, name='register'),
    path('edit/',views.edit_profile, name='edit_profile'),
    path('profile/', views.view_profile, name='view_profile'),
]