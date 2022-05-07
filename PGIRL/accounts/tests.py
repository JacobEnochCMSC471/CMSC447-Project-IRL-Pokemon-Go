from django.test import TestCase
from prometheus_client import instance_ip_grouping_key
from django.test.client import Client
from datetime import datetime
from .models import Profile


class ProfileModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Profile.objects.create(user_id=instance_ip_grouping_key)                                                                                                                                                                                  

    def test_profile(self):                                                                                    
        pass

    # Test user creation
    def test_user_creation(self):
        testUser=Profile.objects.create(user_id=12345, username='katy', image='profile_pics/R.jpg', level=0, experience=0)
        userTest=Profile.objects.get(user_id=12345)
        
        self.assertEqual(testUser, userTest)

    def test_url_exists_at_correct_location(self):
        c=Client()

        response1=c.get('accounts/register')
        response2=c.get('accounts/edit')
        response3=c.get('accounts/profile')

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response3.status_code, 200)
