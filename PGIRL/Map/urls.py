from django.urls import path

from . import views

urlpatterns = [
    path('', views.map, name='map'),
    path('shop', views.shop, name='shop'),
    path('training', views.training, name='training'),
    path('challenges', views.challenges, name='challenges'),
    path('refresh', views.refresh, name='refresh'),
    path('chall', views.chall, name='chall'),
    path('battle_action', views.battle_action, name='battle_action'),
    path('create_challenge', views.create_challenge, name='create_challenge'),
]