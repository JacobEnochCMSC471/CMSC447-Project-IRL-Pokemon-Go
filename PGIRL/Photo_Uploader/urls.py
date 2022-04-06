from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_photo', views.upload_photo_to_db, name='upload_to_db')
]