from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

from . import views
from .views import upload_photo_to_db, success, error

urlpatterns = [
    path('', views.landing_page, name='landing_page'),  # This is the landing page
    path('image_upload/', upload_photo_to_db, name='image_upload'),
    path('image_upload/success', success, name='success'),
    path('image_upload/error', error, name='error')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)