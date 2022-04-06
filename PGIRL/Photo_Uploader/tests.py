from django.test import TestCase
from PGIRL.Photo_Uploader.models import Photo_Data
from django.utils import timezone
import random


class Photo_To_Database(TestCase):

    def setUp(self):
        test_photo = 'photo_example/me.jpg'
        test_id = 1
        date = timezone.now()
        Photo_Data.objects.create(user_id=test_id, image=test_photo, date_added=date)
        random.seed(42)

    def test_photo_defaults(self):
        test1 = Photo_Data.objects.get(user_id=1)
        self.assertEqual(test1.stats_to_str(), '[0, 0, 0, 0]')

        test_values = [None] * 4
        for i in range(4):
            test_values[i] = str(random.randrange(0, 100))

        test1.roll_stats()

        self.assertEqual(test1.stats_to_str(), test_values)



