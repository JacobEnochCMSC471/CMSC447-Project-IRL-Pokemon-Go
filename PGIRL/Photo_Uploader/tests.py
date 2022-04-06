from django.test import TestCase
from Photo_Uploader.models import Photo_Data
from django.utils import timezone
import random
from PIL import Image


class Photo_To_Database(TestCase):

    def setUp(self):
        test_photo = 'photo_example/Me.jpg'
        test_id = 1
        date = timezone.now()
        Photo_Data.objects.create(user_id=test_id, image=test_photo, date_added=date)

    def test_photo_defaults(self):
        print("Test photo object default values")

        test1 = Photo_Data.objects.get(user_id=1)
        self.assertEqual(test1.stats_to_str(), ['0', '0', '0', '0'])

    def test_stat_rolling(self):
        random.seed(42)

        test_values = ['81', '14', '3', '94']

        test1 = Photo_Data.objects.get(user_id=1)

        test1.roll_stats()

        self.assertEqual(test1.stats_to_str(), test_values)
