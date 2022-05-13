from logging import _Level
from django.db import models
from accounts.models import Profile 
from django.contrib.auth.models import User

class userActivity(models.Model):
    def __init__ (self, user, level, experience):
        self.user = user
        self.level = level
        self.experience = experience

        if user.is_active:
            experience+=100
            if (experience>=1000):
                level+=1
