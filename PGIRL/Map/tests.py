from django.test import TestCase
from django.test.client import Client

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MapTester(StaticLiveServerTestCase):
    def test_map_loads(self):
        c = Client()
        response = c.get("/map/")
        self.assertEqual(response.status_code, 200)


    def test_buttons_and_pages(self):
        c = Client()
        #Here we go with serelium again :(
        selenium = webdriver.Chrome(ChromeDriverManager().install())
        selenium.implicitly_wait(0.5)
        selenium.get('%s%s' % (self.live_server_url, '/map/'))

        # Test find all buttons (throws error if it doesn't)
        shop_btn = selenium.find_element_by_id('shop')
        train_btn = selenium.find_element_by_id('training')
        chal_btn = selenium.find_element_by_id('challenges')
        prof_btn = selenium.find_element_by_id('profile')
        print("All buttons found without error.\n")

        #************************************************************************************************
        print("Pressing shop.")
        shop_btn.submit()

        #wait until new page loades (it has a return button), then continue
        WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, "return")))
        response1 = c.get('/map/shop')
        self.assertEqual(response1.status_code, 200)  # Page is up

        print("Shop loaded.")
        #Go back to map
        returnbtn = selenium.find_element_by_id('return')
        returnbtn.submit()

        #should be at map
        response1 = c.get('/map/')
        self.assertEqual(response1.status_code, 200)  # Page is up
        print("Returned to map page.")

        #Repeat for all other buttons (expect profile, it hasn't been implemented yet)
        # Check if the number of passes increased

        # ************************************************************************************************
        WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, "training")))
        print("Pressing training grounds.")
        train_btn = selenium.find_element_by_id('training')
        train_btn.submit()

        # wait until new page loades (it has a return button), then continue
        WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, "return")))
        response1 = c.get('/map/training')
        self.assertEqual(response1.status_code, 200)  # Page is up

        print("Training grounds loaded.")
        # Go back to map
        returnbtn = selenium.find_element_by_id('return')
        returnbtn.submit()

        # should be at map
        response1 = c.get('/map/')
        self.assertEqual(response1.status_code, 200)  # Page is up
        print("Returned to map page.")

        # ************************************************************************************************
        WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, "challenges")))
        print("Pressing challenges button.")
        chal_btn = selenium.find_element_by_id('challenges')
        chal_btn.submit()

        # wait until new page loades (it has a return button), then continue
        WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, "return")))
        response1 = c.get('/map/challenges')
        self.assertEqual(response1.status_code, 200)  # Page is up

        print("Challenges page loaded.")
        # Go back to map
        returnbtn = selenium.find_element_by_id('return')
        returnbtn.submit()

        # should be at map
        response1 = c.get('/map/')
        self.assertEqual(response1.status_code, 200)  # Page is up
        print("Returned to map page.")

        #All tests complete :)
        print("Testing complete :)")
        pass