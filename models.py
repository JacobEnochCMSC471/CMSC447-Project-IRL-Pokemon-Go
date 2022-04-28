from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name=models.CharField(max_length=30,blank=True)
    profile_picture=models.ImageField(default='default.jpg', upload_to='profile_pics')
 #   selected_pet=models.(blank=True)
    level=models.IntegerField(blank=True)
  #  inventory=models.
    experience=models.IntegerField(blank=True)
    
    def __str__(self):
        return f'{self.user.user_name} Profile'

    def save(self):
        super().save()

    