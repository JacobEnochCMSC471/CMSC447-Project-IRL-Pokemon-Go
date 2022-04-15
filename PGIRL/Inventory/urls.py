from django.urls import path

from . import views

urlpatterns = [
    path('', views.select_list, name='select_list'),
    path('inventory/pets/', views.pet_list, name='pet_list'),
    path('inventory/items/', views.item_list, name='item_list'),
]