from django.test import TestCase
from PGIRL.Photo_Uploader.models import Photo_Data
from django.utils import timezone

class Photo_To_Database(TestCase):

    def setUp(self):
        test_photo = 'photo_example/me.jpg'
        user_id = 1
        date_added = timezone.now()


        test1 = Photo_Data()
