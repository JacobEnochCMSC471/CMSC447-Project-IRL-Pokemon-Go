from django.db import models

class Photo_Data(models.model):
    user_id = models.TextField()  # Unique user ID assigned to users when they create an account
    actual_image = models.ImageField()
    date_added = models.DateField()
