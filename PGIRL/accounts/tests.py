from django.test import TestCase
from django.utils import unittest
from django.contrib.auth import get_user_model
from django.test.client import Client
from datetime import datetime
from .models import Profile


class ProfileModelTests(TestCase):
    @classmethod                                                                                                      
    def setUpTestData(cls):                                                                                               
        get_user_model().objects.create()                                                                                                                                                                                   

    def test_profile(self):                                                                                    
        profile = get_user_model().objects.last().profile

    # Test user creation
    def test_user_creation(self):
        testUser=Profile.objects.create(user='katy', image='profile_pics/R.jpg', level=0, experience=0)
        userTest=Profile.objects.get(user='katy')
        print("Entered test")
        self.assertEqual(testUser, userTest)

    def test_url_exists_at_correct_location(self):
        c=Client()

        response1=c.get('accounts/register')
        response2=c.get('accounts/edit')
        response3=c.get('accounts/profile')

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response3.status_code, 200)
