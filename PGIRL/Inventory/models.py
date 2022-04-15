from django.db import models

# Create your models here.
class Item(models.Model):
    user_id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    quantity = models.IntegerField()
    image = models.ImageField()

    def get_user_id(self):
        return self.user_id
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_quantity(self):
        return self.quantity
    
    def get_image(self):
        return self.image
