from django.test import TestCase
from Photo_Uploader.models import Photo_Data
from django.utils import timezone
import random
from django.test.client import Client
from PIL import Image


# Testing documentation: https://django.readthedocs.io/en/1.4.X/topics/testing.html

class Photo_To_Database(TestCase):

    def setUp(self):
        current_time = timezone.now()
        test_photo = 'uploads/kjjcxyighay41.png'
        test_id = 1
        Photo_Data.objects.create(user_id=test_id, image=test_photo, date_added=current_time)
        Photo_Data.objects.create(user_id=2, image='uploads/big_oof.PNG', date_added=current_time)


    def test_photo_defaults(self):
        test1 = Photo_Data.objects.get(user_id=1)

        self.assertEqual(test1.stats_to_str(), ['0', '0', '0', '0'])

    def test_stat_rolling(self):
        print("Testing random stat rolling for photos...\n")

        random.seed(42)

        test_values = ['81', '14', '3', '94']

        test1 = Photo_Data.objects.get(user_id=1)

        test1.roll_stats()

        self.assertEqual(test1.stats_to_str(), test_values)

    def test_model_instance_creation(self):
        print("Testing that databse objects are being created correctly...\n")
        test1 = Photo_Data.objects.get(user_id=1)
        test_image = Image.open(test1.image)
        test_image.show()  # Visual test to see if the image opens correctly

        self.assertEqual(test1.user_id, 1)

    def test_posting_image(self):
        print("Testing client-side requests and responses...\n")
        # First make a request
        c = Client()
        response = c.post('/image_upload', {'user_id': 2, 'image': 'uploads/big_oof.PNG'})
        code = response.status_code
        self.assertEqual(code, 302)

        response = c.get('/success')
        code = response.status_code
        self.assertEqual(code, 200)

        test_2 = Photo_Data.objects.get(user_id=2)

        test_id = test_2.user_id
        self.assertEqual(test_id, 2)

        test_photo = test_2.image
        self.assertEqual(test_photo, 'uploads/big_oof.PNG')

        test_image = Image.open(test_photo)
        test_image.show()




