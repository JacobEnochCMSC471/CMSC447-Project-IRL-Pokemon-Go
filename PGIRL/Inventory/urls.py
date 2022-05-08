from django.urls import path

from . import views

#app_name = 'inventory'

urlpatterns = [
    path('', views.select_list, name='select_list'),
    path('pets/', views.pet_list, name='pet_list'),
    path('pets/<int:user_id>/<str:pet_name>/', views.pet_view, name='pet_view'),
    path('items/', views.item_list, name='item_list'),
]