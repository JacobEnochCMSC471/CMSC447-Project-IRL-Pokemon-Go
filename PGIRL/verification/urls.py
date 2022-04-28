from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from . import views
#import Photo_Uploader.views

urlpatterns = [
    path('', views.verify, name='verify'),
    path('yes', views.answer_yes, name='answer_yes'),
    path('no', views.answer_no, name='answer_no'),
]