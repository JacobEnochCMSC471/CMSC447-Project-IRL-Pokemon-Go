from django.db import models
import random


def get_choices(file):  # Converts all lines in animals.txt file to choices for a dropdown box to be used
    choices = []

    with open(file) as animals:
        for line in animals:
            modified_line = line.strip()
            choices.append((str(modified_line), str(modified_line).upper()))

    animals.close()
    return tuple(choices)


def get_random_name(file):  # Pulls a random name from the names.txt file - used for default pet names
    with open(file) as names:
        file_lines = names.readlines()
        file_length = len(file_lines)

        random_name_line = random.randrange(0, file_length)
        random_name = file_lines[random_name_line]
        random_name = random_name.strip('\n')

    names.close()

    return random_name


class Photo_Data(models.Model):
    animals_txt = 'media/textfiles/animals.txt'
    names_txt = 'media/textfiles/names.txt'

    choices = get_choices(animals_txt)
    random_name = get_random_name(names_txt)

    # Unique user ID assigned to users when they create an account
    user_id = models.CharField(primary_key=False, max_length=150)  # Use the unique username rather than a numerical ID; max length = 30 chars
    pet_name = models.CharField(max_length=25, default=random_name, blank=True)  # Allows people to name the photos they upload
    image = models.ImageField(upload_to='uploads/')  # Directory where photos are uploaded to
    date_added = models.DateField(null=True)  # Date when photos were uploaded
    verified_status = models.BooleanField(default=False)  # Photos will not be verified by default
    user_label = models.CharField(max_length=25, choices=choices, default='None')  # User-supplied label for the image
    strikes = models.IntegerField(default=0)  # Number of times this photo was voted to be incorrectly labelled
    passes = models.IntegerField(default=0) # Number of times this photo was voted to be correctly labelled

    # Each photo will have stats associated with them - these will be automatically rolled when added to the database
    stat_hp = models.IntegerField(default=0)
    stat_attack = models.IntegerField(default=0)
    stat_defense = models.IntegerField(default=0)
    stat_speed = models.IntegerField(default=0)


    def get_stats(self):  # Returns a list of stats in numerical form (hp, attack, defence, speed)
        stats = [self.stat_hp, self.stat_attack, self.stat_defense, self.stat_speed]
        return stats

    def stats_to_str(self):  # Returns a list of stats in string form (hp, attack, defence, speed)
        stats = [str(self.stat_hp), str(self.stat_attack), str(self.stat_defense), str(self.stat_speed)]
        return stats

    def get_verified_status(self):  # Return verified status of photo (default = False)
        return self.verified_status

    def get_date_added(self):  # Get the date of when the photo was added to the database
        return self.date_added

    def get_user_id(self):  # Get the user ID that is associated with the photo
        return self.user_id

    def get_strikes(self):
        return self.strikes

    def get_passes(self):
        return self.passes

    def set_strikes(self, value):
        self.strikes = value

    def set_passes(self, value):
        self.passes = value

    def increment_strikes(self):
        self.strikes += 1

    def increment_passes(self):
        self.passes += 1

    # TODO: Not necessarily MVP but try to find a way to relate stats with the type of animal in photo
    # Example: A turtle would have high defense and hp, mid-range attack and low speed

    def roll_stats(self):  # Randomly rolls and stats for a photo
        random_values = [None] * 4

        for i in range(4):  # Generate a list of 4 random values, ranging between 0 and 100
            random_values[i] = random.randrange(6, 10)

        self.stat_hp = random_values[0]
        self.stat_attack = random_values[1]
        self.stat_defense = random_values[2]
        self.stat_speed = random_values[3]
