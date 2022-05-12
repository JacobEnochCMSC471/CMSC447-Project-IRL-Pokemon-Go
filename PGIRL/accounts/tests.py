from django.test import TestCase
import unittest
from .models import User
from django.contrib.auth import get_user_model
from django.test.client import Client
from datetime import datetime
from .models import Profile


class ProfileModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='katy', email=None, password=None)

    def test_profile(self):
        profile = get_user_model().objects.last().profile

    # Test user creation
    def test_profile_creation(self):
        test_user = User.objects.get(username='katy')
        profile_test1 = Profile.objects.get(user=test_user)

        if profile_test1:  # Test that a profile object is created successfully - if it exists passed = True
            passed = True
        else:
            passed = False

        self.assertEqual(passed, True)

    def test_url_exists_at_correct_location(self):
        test_user = User.objects.get(username='katy')
        c = Client()
        c.force_login(user=test_user, backend=None)

        response1 = c.get('/accounts/register/')
        response2 = c.get('/accounts/edit/')
        response3 = c.get('/accounts/profile/')

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response3.status_code, 200)

    def test_profile_picture_assignment(self):
        from PIL import Image

        test_user = User.objects.get(username='katy')
        test_profile = Profile.objects.get(user=test_user)
        test_profile.profile_picture = 'test_uploads/big_oof.PNG'

        test_image = Image.open(test_profile.profile_picture)

        #test_image.show()

        if test_image:
            passed = True

        else:
            passed = False

        self.assertEqual(passed, True)

    def test_registration_post(self):
        # Registration parameters: username, first_name, last_name, email, password1, password2
        c = Client()
        response = c.post('/accounts/register/', {'username': ['sunnyh3ad'],
                                       'first_name': ['Nina'],
                                       'last_name': ['Vdovicenco'],
                                       'email': ['test@gmail.com'],
                                       'password1': ['welcome12345'],
                                       'password2': ['welcome12345']
                                       })
        code = response.status_code

        self.assertEqual(code, 302)  # Redirect to login page for successful registration
        self.assertRedirects(response, '/login/login/')  # Does it redirect to the right place?

        # Test that the user was registered successfully by checking if the username exists
        try:
            test_user = User.objects.get(username='sunnyh3ad')
            if test_user:
                passed = True

        except User.DoesNotExist:
            passed = False

        self.assertEqual(passed, True)
    