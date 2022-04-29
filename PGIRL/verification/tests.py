#import apocalypse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from Photo_Uploader.models import Photo_Data
from datetime import datetime
from django.test.client import Client
from django.urls import reverse
from django.http import HttpRequest
from verification.views import verify
from django.template.loader import render_to_string

from django.test import LiveServerTestCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#I have no idea why the button tests don't work. When I run the page it works. I'm guessing I need to work on
#serelium more.

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


        #expected_html = render_to_string('verify_pet.html', request=request)
        #self.assertEqual(response2.content.decode(), expected_html)

        #Clear DB
        Photo_Data.objects.all().delete()

        #expected_html = render_to_string('empty_error.html', request=request)
        #self.assertEqual(response2.content.decode(), expected_html)
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
        selenium.implicitly_wait(0.5)
        selenium.get('%s%s' % (self.live_server_url, '/verification/'))


        #Test yes
        #This will throw an error if it can't find the button
        yes_btn = selenium.find_element_by_id('yesbtn')
        print("Yes button found. Continue with the test.\n")

        print("The health was: ", pet1.stat_hp)
        #No error thrown? Let's goo! Pass :)
        print("Pressing yes. You can see the output below.")
        #wait until the information has been recieved
        yes_btn.submit()
        WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, "error_return")))
        pet1 = Photo_Data.objects.get(user_id=1)


        #Check if the number of passes increased
        print("Now its: ", pet1.stat_hp)
        self.assertEqual(pet1.get_passes(), 3)

        self.assertEqual(pet1.verified_status, True)
        self.assertEqual(pet1.stat_hp, init_hp+5)

        #The page should be on defualt error page (no more pets to validate!)
        c = Client()
        response1 = c.get('/verification/')
        self.assertEqual(response1.status_code, 200)  # Page is up

        pass

    # Do the buttons register no view?
    # Do the strikes increase? Is the pet kicked from DB when strikes == threshold (3)
    # Do the passes increase? when pet is verified, does health increase?
    # Does the pet get removed if strikes reaches the threshold?
    def test_vote_no(self):
        # Get the pet
        #pet1 = Photo_Data.objects.get(user_id=1)

        selenium = webdriver.Chrome(ChromeDriverManager().install())
        selenium.implicitly_wait(0.5)
        selenium.get('%s%s' % (self.live_server_url, '/verification/'))
        selenium.set_page_load_timeout(3)


        # This will throw an error if it can't find the button
        nbtn = selenium.find_element_by_id('nobtn')
        print("\'No\' button found. Continue with the test.\n")
        #wait until the information has been recieved
        nbtn.submit()
        WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, "error_return")))

        # No error thrown? Let's goo! Pass :)
        print("Pressing no.")

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
        c = Client()
        response1 = c.get('/verification/')
        self.assertEqual(response1.status_code, 200)  # Page is up

        #expected_html = render_to_string('empty_error.html', request=request)
        #self.assertEqual(response2.content.decode(), expected_html)

        pass

    #Does the Home link work?
    def test_check_exit(self):
        selenium = webdriver.Chrome(ChromeDriverManager().install())
        selenium.implicitly_wait(0.5)
        selenium.get('%s%s' % (self.live_server_url, '/verification/'))
        selenium.set_page_load_timeout(3)

        # This will throw an error if it can't find the button
        selenium.find_element_by_id('home')
        print("Home link found.\n")
        pass

