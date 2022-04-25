from django.test import TestCase
from Photo_Uploader.models import Photo_Data
from datetime import datetime
from django.test.client import Client
from PIL import Image
from io import BytesIO
from django.urls import reverse

# Testing documentation: https://django.readthedocs.io/en/1.4.X/topics/testing.html


class Photo_To_Database(TestCase):

    def setUp(self):
        current_time = datetime.now()
        test_photo = 'uploads/test_image.png'
        Photo_Data.objects.create(user_id=1, image=test_photo, date_added=current_time, user_label="Antelope", verified_status=True,
                                  pet_name='Travis')
        Photo_Data.objects.create(user_id=2, image='uploads/big_oof.PNG', date_added=current_time)

    def test_photo_defaults(self):  # Tests default values for Photo_Data objects
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

    def test_stat_rolling(self):  # Tests to see if stat rolling is working correctly
        # --- Test default test values first --- #
        stat_headers = ['HP', 'Attack', 'Defense', 'Speed']
        test1 = Photo_Data.objects.get(user_id=1)
        test1_stats_1 = test1.get_stats()
        print(test1.stats_to_str(), '\n')

        # --- Test that stat rolling works (random values) --- #
        test1.roll_stats()
        test1_stats_2 = test1.get_stats()
        print(stat_headers)
        print(test1.stats_to_str())

        self.assertNotEqual(test1_stats_1, test1_stats_2)  # Are the rolled stats still default values?

    def test_model_instance_creation(self):
        test1 = Photo_Data.objects.get(user_id=1)
        test_image = Image.open(test1.image)
        test_image.show()  # Visual test to see if the image opens correctly

        self.assertEqual(test1.image, 'uploads/test_image.png')  # Tests that the image path is saved correctly
        self.assertEqual(test1.user_id, 1)  # Tests that the supplied ID was stored correctly

    def test_posting_image(self):
        c = Client()
        response = c.post('/image_upload', {'user_id': ['5'], 'image': 'media/uploads/big_oof.PNG'})
        code = response.status_code
        self.assertEqual(code, 302)  # HTTP 302 indicates a redirect (redirects to /success)

        response = c.get('/success')
        code = response.status_code
        self.assertEqual(code, 200)  # HTTP 200 indicates that the page was sent successfully

    def test_site_functionality(self):
        test = Photo_Data.objects.get(user_id=1)
        c = Client(enforce_csrf_checks=False)

        # I have no idea why this test is failing, my POST matches exactly with posts pulled straight from the site minus a CSRF token
        # It keeps redirecting to /error instead of /success despite being provided the correct things it needs, very confused
        # Example POST pulled from user-generated example by using the site:
        # <QueryDict: {'csrfmiddlewaretoken': ['f7GLFEcLzN3AvKp1jrakIRdwJhn0PAoLZhYBD9WsPXQr8sqNiFEbkRXjYwgwHBsO'], 'user_id': ['123'], 'pet_name': ['Theresa'], 'user_label': ['Aardvark']}>
        # The page is redirected correctly when the page is used by actual people
        # Unsure about how to tackle this thus far after 1.5 hours of hair pulling
        img = BytesIO(b'image')
        img.name = 'media/uploads/test_image.png'
        client_params = {'user_id': ['123'], 'pet_name': ['Theresa'], 'image': img, 'user_label': ['Aardvark']}

        correct_post_response = c.post('/image_upload', client_params)
        incorrect_post_response = c.post('/image_upload', {'user_id': 5, 'image': 'uploads/big_oof.PNG', 'user_label': 'Whale'})

        self.assertRedirects(correct_post_response, '/success')  # Test that successful POST redirects to /success
        self.assertRedirects(incorrect_post_response, '/error')  # Test that a failed POST redirects to /error
        # --- End Rant --- #

        # --- Test that the response for /image_upload uses the correct template
        response = c.get('/image_upload')
        self.assertTemplateUsed(response, 'User_Image_Upload_Form.html')

    def test_directory_links(self): # This tests if the buttons that link to other pages works properly
        c = Client()

        response = c.get('/image_upload')
        self.assertContains(response, '>Home</a></li>')  # Is the Home link rendered properly?
        self.assertContains(response, '>View Inventory</a></li>')  # Is the inventory link rendered properly?

    def test_url_exists_at_correct_location(self):
        c = Client()

        response1 = c.get('/image_upload')
        response2 = c.get('/success')
        response3 = c.get('/error')

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response3.status_code, 200)




