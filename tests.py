from django.test import TestCase

# Note that these tests are also basically placeholders, they won't pass because I'm starting fresh
# Going to have to make new tests for the stuff I actually make myself

class SimpleTest(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

    def test_secure_page(self):
        User = get_user_model()
        self.client.login(username='temporary', password='temporary')
        response = self.client.get('/manufacturers/', follow=True)
        user = User.objects.get(username='temporary')
        self.assertEqual(response.context['email'], 'temporary@gmail.com')