from django.db import models
import random

class Photo_Data(models.Model):

    user_id = models.IntegerField(primary_key=True,
                                  unique=True)  # Unique user ID assigned to users when they create an account
    image = models.ImageField(upload_to='uploads/')
    date_added = models.DateField()
    verified_status = models.BooleanField(default=False)  # Photos will not be verified by default

    # Each photo will have stats associated with them - these will be automatically rolled when added to the database
    stat_hp = models.IntegerField(default=0)
    stat_attack = models.IntegerField(default=0)
    stat_defense = models.IntegerField(default=0)
    stat_speed = models.IntegerField(default=0)

    def stats_to_str(self):
        stats = [str(self.stat_hp), str(self.stat_attack), str(self.stat_defense), str(self.stat_speed)]
        return stats

    def get_verified_status(self):  # Return verified status of photo (default = False)
        return self.verified_status

    def get_date_added(self):  # Get the date of when the photo was added to the database
        return self.date_added

    def get_user_id(self):  # Get the user ID that is associated with the photo
        return self.user_id

    # TODO: Not necessarily MVP but try to find a way to relate stats with the type of animal in photo
    # Example: A turtle would have high defense and hp, mid-range attack and low speed

    def roll_stats(self):  # Randomly rolls and stats for a photo
        random_values = [None] * 4

        for i in range(4):
            random_values[i] = random.randrange(0, 100)

        self.stat_hp = random_values[0]
        self.stat_attack = random_values[1]
        self.stat_defense = random_values[2]
        self.stat_speed = random_values[3]
