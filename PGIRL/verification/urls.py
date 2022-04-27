from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]