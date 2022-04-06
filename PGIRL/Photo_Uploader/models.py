from django.db import models


class Photo_Data(models.Model):
    user_id = models.TextField()  # Unique user ID assigned to users when they create an account
    actual_image = models.ImageField(upload_to='uploads/')
    date_added = models.DateField()
    verified_status = models.BooleanField(default=False)  # Photos will not be verified by default

    # Each photo will have stats associated with them - these will be automatically rolled when added to the database
    stat_hp = models.IntegerField(default=0)
    stat_attack = models.IntegerField(default=0)
    stat_defense = models.IntegerField(default=0)
    stat_speed = models.IntegerField(default=0)
