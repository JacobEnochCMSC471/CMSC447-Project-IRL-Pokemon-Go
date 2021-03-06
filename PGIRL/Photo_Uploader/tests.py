from django.test import TestCase
from Photo_Uploader.models import Photo_Data
from datetime import datetime
from django.test.client import Client
from PIL import Image
from io import BytesIO
from Photo_Uploader.views import remove_bad_photos
from django.urls import reverse
import os
import shutil
import glob


# Testing documentation: https://django.readthedocs.io/en/1.4.X/topics/testing.html


class Photo_To_Database(TestCase):

    def setUp(self):
        current_time = datetime.now()
        test_photo = 'test_uploads/test_image.png'
        Photo_Data.objects.create(user_id='mourgraine', image=test_photo, date_added=current_time, user_label="Antelope", verified_status=True,
                                  pet_name='Travis')  # old id = 1
        Photo_Data.objects.create(user_id='eatdust12', image='test_uploads/big_oof.PNG', date_added=current_time)  # old id = 2
        Photo_Data.objects.create(user_id='XxAnimexX', image='test_uploads/test_2.jpg', date_added=current_time, strikes=6)  # old id = 6
        Photo_Data.objects.create(user_id='urMomLOL', image='test_uploads/test_3.jpg', date_added=current_time, strikes=4)  # old id = 12
        Photo_Data.objects.create(user_id='AshIsDead', image='test_uploads/test_4.jpg', date_added=current_time, strikes=5)  # old id = 18

    def test_photo_defaults(self):  # Tests default values for Photo_Data objects
        test1 = Photo_Data.objects.get(user_id='mourgraine')  # Has a label
        test2 = Photo_Data.objects.get(user_id='eatdust12')  # Has no label
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

    def test_stat_rolling(self):  # Tests to see if stat rolling is working correctly
        # --- Test default test values first --- #
        stat_headers = ['HP', 'Attack', 'Defense', 'Speed']
        test1 = Photo_Data.objects.get(user_id='mourgraine')
        test1_stats_1 = test1.get_stats()
        print(test1.stats_to_str(), '\n')

        # --- Test that stat rolling works (random values) --- #
        test1.roll_stats()
        test1_stats_2 = test1.get_stats()
        print(stat_headers)
        print(test1.stats_to_str())

        self.assertNotEqual(test1_stats_1, test1_stats_2)  # Are the rolled stats still default values?

    def test_model_instance_creation(self):
        test1 = Photo_Data.objects.get(user_id='mourgraine')
        test_image = Image.open(test1.image)
        # test_image.show()  # Visual test to see if the image opens correctly

        self.assertEqual(test1.image, 'test_uploads/test_image.png')  # Tests that the image path is saved correctly
        self.assertEqual(test1.user_id, 'mourgraine')  # Tests that the supplied ID was stored correctly
        test_image.close()  # Close the image after being used

    def test_posting_image(self):
        c = Client()
        img = BytesIO(b'test_image')
        img.name = 'media/test_uploads/test_5.jpg'

        with open(img.name, 'rb') as fp:
            response = c.post('/image_upload/', {'user_id': '123', 'pet_name': 'Theresa', 'user_label': 'Aardvark', 'image': fp})

        file_name = os.path.split(img.name)  # splits filepath into head/tail - tail = actual file

        if os.path.exists('media/uploads/' + file_name[1]):  # Delete trash image after it's posted
            os.remove('media/uploads/' + file_name[1])

        fp.close()

        code = response.status_code
        self.assertEqual(code, 302)  # HTTP 302 indicates a redirect (should redirect to /success)
        self.assertRedirects(response, '/image_upload/success')

    def test_site_functionality(self):
        test = Photo_Data.objects.get(user_id='mourgraine')
        c = Client()
        img = BytesIO(b'test_image')
        img.name = 'media/' + str(test.image)

        '''
        # I have no idea why this test is failing, my POST matches exactly with posts pulled straight from the site minus a CSRF token
        # It keeps redirecting to /error instead of /success despite being provided the correct things it needs, very confused
        # Example POST pulled from user-generated example by using the site:
        # <QueryDict: {'csrfmiddlewaretoken': ['f7GLFEcLzN3AvKp1jrakIRdwJhn0PAoLZhYBD9WsPXQr8sqNiFEbkRXjYwgwHBsO'], 'user_id': ['123'], 'pet_name': ['Theresa'], 'user_label': ['Aardvark']}>
        # The page is redirected correctly when the page is used by actual people
        # Unsure about how to tackle this thus far after 1.5 hours of hair pulling
        # --- End Rant --- #
        
        4/25 - finally fixed!!!! :))))
        '''

        with open(img.name, 'rb') as fp:
            correct_post_response = c.post('/image_upload/', {'user_id': '123', 'pet_name': 'Theresa', 'user_label': 'Aardvark', 'image': fp})
            incorrect_post_response = c.post('/image_upload/', {'user_id': 5, 'image': fp, 'user_label': 'Whale'})

        file_name = os.path.split(img.name)  # splits filepath into head/tail - tail = actual file

        if os.path.exists('media/uploads/' + file_name[1]):  # Delete trash image after it's posted
            os.remove('media/uploads/' + file_name[1])

        fp.close()  # Close the filepath

        self.assertRedirects(correct_post_response, '/image_upload/success')  # Test that successful POST redirects to /success
        self.assertRedirects(incorrect_post_response, '/image_upload/error')  # Test that a failed POST redirects to /error

        # --- Test that the response for /image_upload uses the correct template
        response = c.get('/image_upload/')
        self.assertTemplateUsed(response, 'User_Image_Upload_Form.html')

    def test_url_exists_at_correct_location(self):
        c = Client()

        response1 = c.get('/image_upload/')
        response2 = c.get('/image_upload/success')
        response3 = c.get('/image_upload/error')

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response3.status_code, 200)

    def test_photo_removal(self):  # Tests that photos with strikes past a certain threshold are removed from the DB and uploads directory
        photo_removal_threshold = 5  # If a photo object gets at least this many strikes remove it
        current_time = datetime.now()

        test_2_photo = 'media/' + str(Photo_Data.objects.get(user_id='XxAnimexX').image)
        test_3_photo = 'media/' + str(Photo_Data.objects.get(user_id='AshIsDead').image)

        current_db = Photo_Data.objects.all()

        total_items = 0

        for photo in current_db.iterator():
            total_items += 1

        self.assertEqual(total_items, 5)  # 4 items in DB before any deletes occur

        remove_bad_photos(photo_removal_threshold)

        current_db = Photo_Data.objects.all()

        total_items = 0

        for photo in current_db.iterator():
            print(photo)
            total_items += 1

        self.assertEqual(total_items, 3)  # 3 items in DB after deletes

        photo_exist_test2 = True
        photo_exist_test3 = True

        if not os.path.exists(test_2_photo):
            photo_exist_test2 = False

        if not os.path.exists(test_3_photo):
            photo_exist_test3 = False

        self.assertEqual(photo_exist_test2, False)
        self.assertEqual(photo_exist_test3, False)

    def tearDown(self):
        backup_path = 'media/test_uploads_copy'
        test_path = 'media/test_uploads'
        shutil.rmtree(test_path)  # Delete the test image directory
        shutil.copytree(backup_path, test_path)  # Copy files from test backup to new test directory so files stay after test
