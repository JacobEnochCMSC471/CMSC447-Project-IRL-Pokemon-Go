from django.test import TestCase
from django.test.client import Client

class MapTester(TestCase):
    def test_map_loads(self):
        c = Client()
        response = c.get("/map/")
        self.assertEqual(response.status_code, 200)