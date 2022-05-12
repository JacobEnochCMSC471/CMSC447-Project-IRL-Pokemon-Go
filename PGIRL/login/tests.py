from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test.client import Client
from accounts.models import User

# Create your tests here.
@classmethod
class LoginTests(TestCase):
    def setUpTestData(cls):
        User.objects.create_user(user_name='Big_Jeff', email=None, password='welcome12345')


