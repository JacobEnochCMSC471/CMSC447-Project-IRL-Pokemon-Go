from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from Inventory.models import Item


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default.jpg', upload_to='accounts/profile_pics')
    # selected_pet=models.user_id.Inventory(blank=True)
    level = models.IntegerField(default=0)
    inventory = Item.user_id
    experience = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = Profile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=User)

    def get_user(self):
        return self.user

    def get_profilePicture(self):
        return self.profile_picture

    def get_level(self):
        return self.level

    def get_experience(self):
        return self.experience
