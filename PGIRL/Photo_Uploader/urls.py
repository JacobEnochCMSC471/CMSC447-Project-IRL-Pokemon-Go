from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

from . import views
from .views import upload_photo_to_db, success

urlpatterns = [
    path('', views.index, name='index'),
    path('image_upload', upload_photo_to_db, name='image_upload'),
    path('success', success, name='success'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)