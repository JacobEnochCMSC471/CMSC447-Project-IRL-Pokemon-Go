from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from . import views
#import Photo_Uploader.views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.answer_yes, name='answer_yes'),
    path('', views.answer_no, name='answer_no'),
]