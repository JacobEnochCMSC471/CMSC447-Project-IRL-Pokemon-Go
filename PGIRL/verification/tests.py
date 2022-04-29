#from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from Photo_Uploader.models import Photo_Data
from datetime import datetime
from django.test.client import Client
from django.urls import reverse
from PIL import Image
from io import BytesIO
from django.http import HttpRequest
from verification.views import verify

from django.test import LiveServerTestCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Create your tests here. This should run the server alongside testing.. for selenium.
class VerifyTest(StaticLiveServerTestCase):

    def setUp(self):
        #add these to the DB
        current_time = datetime.now()
        Photo_Data.objects.all().delete()
        Photo_Data.objects.create(user_id=1, image='test_uploads/big_oof.PNG', date_added=current_time, strikes=2,passes=2)
        pass

    #Am I sent to the error screen if nothing's in the DB?
    def test_site(self):
        c = Client()
        response1 = c.get('/verification/')
        self.assertEqual(response1.status_code, 200) #Page is up

        # Is this the right page tho
        request = HttpRequest()
        response2 = verify(request)
        expected_html = render_to_string('verify_pet.html', request=request)
        self.assertEqual(response2.content.decode(), expected_html)

        #Clear DB
        Photo_Data.objects.all().delete()

        #empty page?
        request = HttpRequest()
        response2 = verify(request)
        expected_html = render_to_string('empty_error.html', request=request)
        self.assertEqual(response2.content.decode(), expected_html)
        pass

    #backup option
    def test_here(self):
        #does this work? idk let's find out :)
        #self.assertTemplateUsed(self.response, 'verify_pet.html')
        pass

    #Do the buttons register yes view?
    #Do the passes increase? when pet is verified, does health increase?
    #Do we go to empty_error.html when 3 passes reached?
    def test_voting_yes(self):
        #Get the pet
        pet1 = Photo_Data.objects.get(user_id=1)
        init_hp = pet1.stat_hp

        selenium = webdriver.Chrome(ChromeDriverManager().install())
        selenium.get('%s%s' % (self.live_server_url, '/verification/'))

        #Test yes
        #This will throw an error if it can't find the button
        yes_btn = selenium.find_element_by_id('yesbtn')
        print("Yes button found. Continue with the test.\n")

        print("Number of passes was: ", pet1.get_passes())
        #No error thrown? Let's goo! Pass :)
        print("Pressing yes.")
        yes_btn.click()

        #Check if the number of passes increased
        print("Now its: ", pet1.get_passes())
        self.assertEqual(pet1.get_passes(), 3, "Passes incremented correctly")

        self.assertEqual(pet1.verified_status, True, "Verification flag flipped.")
        self.assertEqual(pet1.stat_hp, init_hp+5, "Health Boost Applied.")

        #The page should be on defualt error page (no more pets to validate!)
        request = HttpRequest()
        response2 = home_page(request)
        expected_html = render_to_string('empty_error.html', request=request)
        self.assertEqual(response2.content.decode(), expected_html)

        pass

    # Do the buttons register no view?
    # Do the strikes increase? Is the pet kicked from DB when strikes == threshold (3)
    # Do the passes increase? when pet is verified, does health increase?
    # Does the pet get removed if strikes reaches the threshold?
    def test_vote_no(self):
        # Get the pet
        #pet1 = Photo_Data.objects.get(user_id=1)

        selenium = webdriver.Chrome(ChromeDriverManager().install())
        selenium.get('%s%s' % (self.live_server_url, '/verification/'))

        # This will throw an error if it can't find the button
        no_btn = selenium.find_element_by_id('nobtn')
        print("\'No\' button found. Continue with the test.\n")

        # No error thrown? Let's goo! Pass :)
        print("Pressing no.")
        no_btn.click()

        #If strikes increased correctly, the pet is deleted from existence. Reduced to atoms.
        #DB should be empty
        queryset = Photo_Data.objects.all()

        if queryset.exists():
            print("L test failed")
            self.assertEqual(1,2)
            pass
        else:
            print("Nice! Photo has been destroyed.")
            self.assertEqual(1, 1)
            pass

        # The page should be on default error page (no more pets to validate!)
        request = HttpRequest()
        response2 = verify(request)
        expected_html = render_to_string('empty_error.html', request=request)
        self.assertEqual(response2.content.decode(), expected_html)

        pass

    #Does the Home link work?
    def test_check_exit(self):
        selenium = webdriver.Chrome()
        selenium.get('http://127.0.0.1:8000/verification/')
        # This will throw an error if it can't find the button
        elenium.find_element_by_id('home')
        print("\'No\' button found. Continue with the test.\n")
        pass

