from django.urls import path, include
from . import views

urlpatterns = [
    path('accepted/',views.view_accepted_challenges, name = 'view_accepted_challenges'),
    path('list/',views.available_challenges, name = 'available_challenges'),
]