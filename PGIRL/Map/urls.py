from django.urls import path

from . import views

urlpatterns = [
    path('', views.map, name='map'),
    path('shop', views.shop, name='shop'),
    path('training', views.training, name='training'),
    path('challenges', views.challenges, name='challenges'),
]