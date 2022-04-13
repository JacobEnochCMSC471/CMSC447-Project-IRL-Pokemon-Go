from django.test import TestCase
from Photo_Uploader.models import Photo_Data
from django.utils import timezone
from django.test.client import Client
from PIL import Image


# Testing documentation: https://django.readthedocs.io/en/1.4.X/topics/testing.html

class Photo_To_Database(TestCase):

    def setUp(self):
        current_time = timezone.now()
        test_photo = 'uploads/test_image.png'
        Photo_Data.objects.create(user_id=1, image=test_photo, date_added=current_time, user_label="Antelope", verified_status=True, pet_name='Travis')
        Photo_Data.objects.create(user_id=2, image='uploads/big_oof.PNG', date_added=current_time)

    def test_photo_defaults(self):
        test1 = Photo_Data.objects.get(user_id=1)  # Has a label
        test2 = Photo_Data.objects.get(user_id=2)  # Has no label
        self.assertEqual(test1.stats_to_str(), ['0', '0', '0', '0'])  # Should instantiate as all 0's

        # --- Test User 1 (no default values except stats) --- #
        self.assertEqual(test1.user_label, 'Antelope')  # User supplied Antelope label
        self.assertEqual(test1.verified_status, True)
        self.assertEqual(test1.pet_name, 'Travis')

        # --- Test User 2 (All possible default values) --- #
        self.assertEqual(test2.user_label, 'None')  # User provided no label
        print('Test 2 Name: ', test2.pet_name)  # Visual inspection to make sure names are created correctly
        self.assertEqual(test2.verified_status, False)
        self.assertEqual(test2.user_label, 'None')


    def test_stat_rolling(self):
        print("Testing random stat rolling for photos...\n")
        stat_headers = ['HP', 'Attack', 'Defense', 'Speed']
        test1 = Photo_Data.objects.get(user_id=1)
        test1_stats_1 = test1.get_stats()
        print("Before stat rolling:")
        print(stat_headers)
        print(test1.stats_to_str(), '\n')

        print("After stat rolling:")
        test1.roll_stats()
        test1_stats_2 = test1.get_stats()
        print(stat_headers)
        print(test1.stats_to_str())

        self.assertNotEqual(test1_stats_1, test1_stats_2)

    def test_model_instance_creation(self):
        print("Testing that databse objects are being created correctly...\n")
        test1 = Photo_Data.objects.get(user_id=1)
        test_image = Image.open(test1.image)
        test_image.show()  # Visual test to see if the image opens correctly
        self.assertEqual(test1.image, 'uploads/test_image.png')

        self.assertEqual(test1.user_id, 1)

    def test_posting_image(self):
        print("Testing client-side requests and responses...\n")

        c = Client()
        response = c.post('/image_upload', {'user_id': 5, 'image': 'uploads/big_oof.PNG', 'label': 'Whale'})
        code = response.status_code
        self.assertEqual(code, 302)  # HTTP 302 indicates a redirect (redirects to /success)

        response = c.get('/success')
        code = response.status_code
        self.assertEqual(code, 302)  # HTTP 302 indicates a redirect (redirects to image_upload)
