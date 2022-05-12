from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test.client import Client
from accounts.models import User


# Create your tests here.
class LoginTests(TestCase):
    def setUp(self):
        User.objects.create_user(username='Big_Jeff', email=None, password='welcome12345')

    def test_user_login(self):
        try:
            test_user = User.objects.get(username='Big_Jeff')
            if test_user:
                passed = True

        except User.DoesNotExist:
            passed = False

        self.assertEqual(passed, True)

        c = Client()
        test1 = c.login(username='Big_Jeff', password='welcome12345')

        self.assertEqual(test1, True)  # Did the user login successfully?

    def test_hidden_login_stuff_logged_in(self):  # Tests that the correct Navbar items are hidden when a user is logged in
        try:
            test_user = User.objects.get(username='Big_Jeff')
            if test_user:
                passed = True

        except User.DoesNotExist:
            passed = False

        self.assertEqual(passed, True)

        c = Client()
        c.login(username='Big_Jeff', password='welcome12345')
        response = c.get('')

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Home')
        self.assertContains(response, 'Inventory')
        self.assertContains(response, 'verify')
        self.assertContains(response, 'map')
        self.assertContains(response, 'View Profile')
        self.assertContains(response, 'Edit Profile')
        self.assertContains(response, 'logout')

        self.assertNotContains(response, 'Make an account')  # Users who are logged in should not be prompted to register
        self.assertNotContains(response, 'Login')  # Users who are logged in already should not be prompted to log in

        test2 = c.logout()

    def test_hidden_login_stuff_logged_out(self):  # Tests that the correct Navbar items are hidden when a user is logged out
        try:
            test_user = User.objects.get(username='Big_Jeff')
            if test_user:
                passed = True

        except User.DoesNotExist:
            passed = False

        self.assertEqual(passed, True)

        c = Client()
        response2 = c.get('')

        self.assertNotContains(response2, 'Inventory')
        self.assertNotContains(response2, 'map')
        self.assertNotContains(response2, 'View Profile')
        self.assertNotContains(response2, 'Edit Profile')
        self.assertNotContains(response2, 'logout')

        self.assertContains(response2, 'Home')
        self.assertContains(response2, 'verify')
        self.assertContains(response2, 'Make an account')  # Users who are logged in should not be prompted to register
        self.assertContains(response2, 'Login')  # Users who are logged in already should not be prompted to log in

    def test_correct_locations(self):
        c = Client()
        response1 = c.get('/login/login/')
        self.assertEqual(response1.status_code, 200)

        response2 = c.get('/login/password_reset/')
        self.assertEqual(response2.status_code, 200)

        response3 = c.get('/login/logout/')
        self.assertEqual(response3.status_code, 302)  # Redirects somewhere
        self.assertRedirects(response3, '/')  # Does it redirect to the correct place?
