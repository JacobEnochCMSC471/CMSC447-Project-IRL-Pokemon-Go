from django.test import TestCase
from Photo_Uploader.models import Photo_Data
from datetime import datetime
from django.test.client import Client
from django.urls import reverse
from PIL import Image
from io import BytesIO

# Create your tests here.
class VerifyTest(self):
    #test if the site is up
    def test_here(self):
        response = self.client.get(reverse('verify'))
        self.assertEqual(response.status_code, 200)
        pass

    #set up 2 pets (one to pass one to fail)
    def test_start(self):
        pass

    #Am I sent to the error screen if nothing's in the DB?
    def test_empty_db(self):
        pass

    #Do the page/images load?
    def test_vote(self):
        pass

    #Do the strikes increase?
    def test_check_strikes(self):
        pass

    #Do the passes increase?
    def test_check_passes(self):
        pass

    #Am I returned to the home page?
    def test_check_exit(self):
        pass