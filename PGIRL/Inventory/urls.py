from django.urls import path

from . import views

urlpatterns = [
    path('', views.select_list, name='select_list'),
    path('pets/', views.pet_list, name='pet_list'),
    path('items/', views.item_list, name='item_list'),
]