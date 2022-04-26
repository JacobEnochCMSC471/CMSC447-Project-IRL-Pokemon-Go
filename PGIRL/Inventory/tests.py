from datetime import datetime
from django.test import TestCase
from django.test.client import Client

from .models import Item
from Photo_Uploader.models import Photo_Data

# Create your tests here.
class InventoryTester(TestCase):

    # Test for an ok response when there are no pets
    def test_empty_pet_list(self):
        c = Client()
        response = c.get('/inventory/pets/')
        code = response.status_code
        self.assertEqual(code, 200)
    
    # Test for an ok response when there are no items
    def test_empty_item_list(self):
        c = Client()
        response = c.get('/inventory/items/')
        code = response.status_code
        self.assertEqual(code, 200)
    
    # Test that items are stored correctly in the database
    def test_item_creation(self):
        testItem = Item.objects.create(user_id=1, name='Potion', description="Heals your pet for 5 billion hp", quantity=1, image='uploads/big_oof.PNG')
        itemTest = Item.objects.get(user_id=1)
        self.assertEqual(testItem, itemTest)
    
    # Test that items get displayed in the item list
    def test_item_list(self):
        item1: Item = Item.objects.create(user_id=1, name='Potion', description="Heals your pet for 5 billion hp", quantity=1, image='uploads/big_oof.PNG')
        item2: Item = Item.objects.create(user_id=2, name='Jules Potion', description="Turns your pet into the mighty Jules permanently", quantity=9999, image='uploads/test_image.png')

        c = Client()
        response = c.get('/inventory/items/')
        raw_html = response.content
        test1 = False
        test2 = False
        # encode strings as bytestrings to match against the raw html
        if (item1.name).encode() in raw_html and (item1.description).encode() in raw_html:
            test1 = True
        if (item2.name).encode() in raw_html and (item2.description).encode() in raw_html:
             test2 = True
            
        self.assertEqual(test1, True)
        self.assertEqual(test2, True)

    
    # Test that pets get displayed in the pet list
    def test_pet_list(self):
        pet1 = Photo_Data.objects.create(user_id=1, image='uploads/big_oof.PNG', date_added=datetime.now(), user_label="Ant", verified_status=True, pet_name='Jim')
        pet2 = Photo_Data.objects.create(user_id=2, image='uploads/test_image.png', date_added=datetime.now(), user_label="Alpaca", verified_status=True, pet_name='Susie')

        c = Client()
        response = c.get('/inventory/pets/')
        raw_html = response.content
        test1 = False
        test2 = False
        # encode strings as bytestrings to match against the raw html
        if (pet1.pet_name).encode() in raw_html:
            test1 = True
        if (pet2.pet_name).encode() in raw_html:
                test2 = True
            
        self.assertEqual(test1, True)
        self.assertEqual(test2, True)