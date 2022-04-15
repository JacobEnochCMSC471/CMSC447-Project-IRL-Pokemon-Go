from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/',include('profile.urls')),
  #  path('__debug__/', include('debug_toolbar.urls')),
]